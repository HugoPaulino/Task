
from pymongo import MongoClient
import psycopg2
import collections
import logging

class database(object):
    def __init__(self):
        # Connect to existing database
        #TODO change this to a ini file a load it with config parser
        self.sql_conn = psycopg2.connect(
            database="productdb",
            user="docker",
            password="docker",
            host="postgresdb",
            port="5432"
        )
        mongo_client = MongoClient(host ="mongodb:27017", username='root', password='root')
        mydb = mongo_client["productskpis_db"]
        self.collection = mydb["productkpis_results"]    


    def price_rank_grouped_by_brand(self):
        cur = self.sql_conn.cursor()

        # Query the database 
        cur.execute("SELECT price, RANK() OVER ( PARTITION BY brand ORDER BY price DESC ) pricerank FROM product GROUP BY brand, price")
        rows = cur.fetchall()

        docArray = []
        for row in rows:
            doc = collections.OrderedDict()
            doc['price'] = row[0]
            doc['rank'] = row[1]
            docArray.append(doc)
            #print(row)
        self.collection.insert_many(docArray)
        
        print("Price Rank grouped by brand")


    def min_hdd_gb(self):
        
        cur = self.sql_conn.cursor()

        # Query the database 
        docArray = []
        cur.execute("SELECT MIN(hdd_gb) FROM product")
        rows = cur.fetchone()
        print(rows)
        doc = collections.OrderedDict()
        doc['max_price'] = rows[0]
        #docArray.append(doc)
        
        self.collection.insert_one(doc)
        #for row in rows:
        #    print(row)
        print("Max hdd_gb")

    def max_hdd_gb(self):
        
        cur = self.sql_conn.cursor()

        # Query the database 
        docArray = []
        cur.execute("SELECT MAX(hdd_gb) FROM product")
        rows = cur.fetchone()
        doc = collections.OrderedDict()
        doc['max_price'] = rows[0]
        #docArray.append(doc)
        
        self.collection.insert_one(doc)
        #for row in rows:
        #    print(row)

        print("Max hdd_gb")

    def ghz_median_grouped_by_ramgb(self):
        
        cur = self.sql_conn.cursor()

        # Query the database  
        cur.execute("SELECT avg(ghz) as median_ghz,ram_gb FROM product group by ram_gb")
        
        rows = cur.fetchall()
        docArray = []
        for row in rows:
            doc = collections.OrderedDict()
            doc['median_ghz'] = row[0]
            doc['ram_gb'] = row[1]
            docArray.append(doc)

        self.collection.insert_many(docArray)
        
        print("Max hdd_gb")



    def main(self):


        # Response question 3a
        self.price_rank_grouped_by_brand()

        # Response question 3b
        self.min_hdd_gb()
        self.max_hdd_gb()

        # Response question 3c
        self.ghz_median_grouped_by_ramgb()

        # Close communications with database
        self.cur.close()
        self.conn.close()
        # Open cursor to perform database operation
        #cur = self.conn.cursor()


        # Query the database 
        #cur.execute("SELECT * FROM product limit 1")
        #rows = cur.fetchall()
        #for row in rows:
        #    print(row)

        # Query the database 
        #cur.execute("SELECT RANK() OVER(PARTITION BY a.price ORDER BY a.brand) AS rnk")
        #rows = cur.fetchall()
        #for row in rows:
        #    print(row)

    
if __name__ == "__main__":
    print("Aplication startup")


    database().main()
