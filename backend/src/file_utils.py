import os
from src.logger import logging
from urllib.parse import urlparse
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from params import *
import shutil


def run_db_build(chat_id, env, encoder):

    if not os.path.exists(f'{DB_FAISS_PATH}/{env}_{chat_id}'):
        os.makedirs(f'{DB_FAISS_PATH}/{env}_{chat_id}')
        logging.info(f"Folder '{f'{DB_FAISS_PATH}/{env}_{chat_id}'}' created.")

        # file_list = os.listdir(f'{DATA_PATH}/{env}_{chat_id}')
        # txt_files = [file for file in file_list if file.endswith(".txt")]

        # files = []
        # for file in txt_files:
        #     with open(f'{DATA_PATH}/{env}_{chat_id}/{file}', 'r', encoding='utf-8') as f:
        #         state_of_the_union = f.read()
        #         files.append(state_of_the_union)

        loader = DirectoryLoader(f'{DATA_PATH}/{env}_{chat_id}', glob="*.txt")

        files = loader.load()

        logging.info("Load all files to create Vector Database")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,
                                                       chunk_overlap=CHUNK_OVERLAP)

        texts = text_splitter.split_documents(files)
        # texts = text_splitter.create_documents(files)
        logging.info("Create chunks using text splitter")

        vectorstore = FAISS.from_documents(texts, encoder)
        vectorstore.save_local(f'{DB_FAISS_PATH}/{env}_{chat_id}')

        full_text = ""
        for text in texts:
            full_text += (" " + text.page_content)

        number_of_embedding_tokens = num_tokens_from_string(
            full_text, ENCODING_NAME)

        logging.info("Save files into Vector Database")
        return number_of_embedding_tokens
    else:
        logging.info(
            f"Folder '{f'{DB_FAISS_PATH}/{env}_{chat_id}'}' already exists.")
        return 0


def download_files(chat_id, file_url_list, env):
    if not os.path.exists(f'{DATA_PATH}{env}_{chat_id}'):
        os.makedirs(f'{DATA_PATH}{env}_{chat_id}')
        logging.info(f"Folder '{f'{DATA_PATH}{env}_{chat_id}'}' created.")
        for file_url in file_url_list:

            parsed_url = urlparse(file_url)
            path_segments = parsed_url.path.strip("/").split("/")
            container_name = path_segments[0]
            blob_name = "/".join(path_segments[1:])
            file_name = blob_name.split("/")[-1]

            blob_client = blob_service_client1.get_blob_client(
                container=container_name, blob=blob_name)
            with open(f"{DATA_PATH}{env}_{chat_id}/{file_name}", "wb") as f:
                download_stream = blob_client.download_blob()
                f.write(download_stream.readall())
                logging.info(f'Downloaded file: {f}')
    else:
        logging.info(f"Folder '{f'{DATA_PATH}{chat_id}'}' already exists.")


def remove_folder(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        try:
            shutil.rmtree(directory_path)
            logging.info(f"Directory '{directory_path}' has been removed.")
        except OSError as e:
            logging.info(f"Error while removing directory: {e}")
    else:
        logging.info(f"Directory '{directory_path}' does not exist.")


def remove_folder_structure(chat_id, env):
    directory_path_to_data = f'{DATA_PATH}{env}_{chat_id}'
    directory_path_to_vectordb = f'{DB_FAISS_PATH}/{env}_{chat_id}'

    remove_folder(directory_path_to_data)
    remove_folder(directory_path_to_vectordb)


def build_folder_structure(chat_id, file_url_list, env, encoder):
    download_files(chat_id, file_url_list, env)
    number_of_embedding_tokens = run_db_build(chat_id, env, encoder)
    return number_of_embedding_tokens
