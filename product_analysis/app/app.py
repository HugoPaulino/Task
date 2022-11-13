
from pymongo import MongoClient
import psycopg2
import collections

class Database():
    """
    A class to represent a database with respective connections and queries.

    Attributes
    ----------

    Methods
    -------
    price_rank_grouped_by_brand(self):
        Gets product data from Posgresdb and execute the ranking 
        based on price grouped by brand
    min_hdd_gb(self):
        Gets product data from Posgresdb and executes the min of hdd_gb column
    max_hdd_gb(self):
        Gets product data from Posgresdb and executes the max of hdd_gb column
    ghz_median_grouped_by_ramgb(self):
        Gets product data from Posgresdb and execute the median of the ghz 
        grouped by ram_gb
        """


    def __init__(self):
        # Connect to existing database
        #TODO change this to a ini file a load it with config parser

        """
        Constructs all the necessary attributes for the database object.

        Parameters
        ----------
        """
        self.sql_conn = psycopg2.connect(
            database="productdb",
            user="docker",
            password="docker",
            host="postgresdb",
            port="5432"
        )
        mongo_client = MongoClient(host ="mongodb:27017", username='root', password='root')
        self.mydb = mongo_client["productskpis_db"]
        #self.collection = mydb["productkpis_results"]    


    def price_rank_grouped_by_brand(self):
        """
        Gets data from product table and preform a ranking query based on price grouped by brand
        Inserts the results on mongodb

        Parameters
        ----------
        self : object 
            Constructor object containing db.

        Returns
        -------
        None
        """
        cur = self.sql_conn.cursor()

        cur.execute("SELECT price, RANK() OVER ( ORDER BY price ASC ) pricerank FROM product GROUP BY brand, price")
        rows = cur.fetchall()

        docArray = []
        for row in rows:
            doc = collections.OrderedDict()
            doc['price'] = row[0]
            doc['rank'] = row[1]
            docArray.append(doc)
        collection = self.mydb["productkpis_results_3a"]
        collection.insert_many(docArray)

    def min_hdd_gb(self):
        """
        Gets data from product table and preform a min query based on hdd_gb column.
        Inserts the results on mongodb

        Parameters
        ----------
        self : object 
            Constructor object containing db connections.

        Returns
        -------
        None
        """
        cur = self.sql_conn.cursor()

        # Query the database 
        cur.execute("SELECT MIN(hdd_gb) FROM product")
        rows = cur.fetchone()

        doc = collections.OrderedDict()
        doc['min_hdd_gb'] = rows[0]
        collection = self.mydb["productkpis_results_3b1"]
        collection.insert_one(doc)

    def max_hdd_gb(self):
        """
        Gets data from product table and preform a max query based on hdd_gb column.
        Inserts the results on mongodb

        Parameters
        ----------
        self : object 
            Constructor object containing db connections.

        Returns
        -------
        None
        """
        cur = self.sql_conn.cursor()

        # Query the database 
        cur.execute("SELECT MAX(hdd_gb) FROM product")
        rows = cur.fetchone()
        doc = collections.OrderedDict()
        doc['max_hdd_gb'] = rows[0]
        collection = self.mydb["productkpis_results_3b2"]
        collection.insert_one(doc)

    def ghz_median_grouped_by_ramgb(self):
        """
        Gets data from product table and preform a median query based on ghz column grouped by ramgb.
        Inserts the results on mongodb

        Parameters
        ----------
       self : object 
            Constructor object containing db connections.

        Returns
        -------
        None
        """
        cur = self.sql_conn.cursor()

        # Query the database  
        cur.execute("SELECT avg(ghz) as median_ghz,ram_gb FROM product group by ram_gb")
        
        rows = cur.fetchall()
        docArray = []
        for row in rows:
            doc = collections.OrderedDict()
            doc['median_ghz'] = str(row[0])
            doc['ram_gb'] = row[1]
            docArray.append(doc)
        collection = self.mydb["productkpis_results_3c"]
        collection.insert_many(docArray)

    def main(self):
        """
        Executes all the query and insert functions sequentialy.

        Parameters
        ----------
        self : object 
            Constructor object containing db connections.

        Returns
        -------
        None
        """
        # Response question 3a
        self.price_rank_grouped_by_brand()

        # Response question 3b
        self.min_hdd_gb()
        self.max_hdd_gb()

        # Response question 3c
        self.ghz_median_grouped_by_ramgb()

        # Close communication with database
        self.sql_conn.close()
    
if __name__ == "__main__":
    print("Aplication startup")

    #initiate db connections
    database_obj = Database()

    # perform queries and save the results in mongodb
    database_obj.main()
    