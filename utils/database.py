import pandas as pd
import pymongo
import urllib
import streamlit as st

def get_mongo_client(config):
    """Get the mongo client and store it in cache.

        Params
        ------
        config : Config
            Configuration object containing email details.
        
        Returns
        -------
        client
            The mongo client connected to the database.
        """
    db_mongo = config.get_config()['db_mongo']
    user = db_mongo["user"]
    password = urllib.parse.quote_plus(db_mongo["password"])
    cluster = db_mongo["cluster"]
    client = pymongo.MongoClient(
        f"mongodb+srv://{user}:{password}@{cluster}/?retryWrites=true&w=majority"
    )
    return client
