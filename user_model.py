from mysqlconnection import connectToMySQL

class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.cupdated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM users;"""

        results = connectToMySQL(cls.DB).query_db(query)

        all_users = []

        for user in results:
            all_users.append(cls(user))

        return all_users
    
    @classmethod
    def add_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return results