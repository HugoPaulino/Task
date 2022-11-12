


def test_get_product(get_database):
    db = get_database
    #db.fetchone("SELECT COUNT(*) FROM users")
    row = db.fetchone("SELECT COUNT(*) FROM product")
    print("Num of records: ", row[0])


#def test_insert_product():
    