from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot be blank'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be blank'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "User with '{}' already exits".format(data['username'])}, 400
            # return {'message': "User with '" + data['username'] + "' already exits"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201  # 201: created
