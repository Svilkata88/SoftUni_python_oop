from project.user import User
from project.library import Library


class Registration:
    @staticmethod
    def add_user(user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    @staticmethod
    def remove_user(user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        for user_obj in library.user_records:
            if user_obj.user_id == user_id:
                if user_obj.username != new_username:
                    for element in library.rented_books.keys():
                        if element == user_obj.username:
                            user_obj.username = new_username
                    user_obj.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                return f"Please check again the provided " \
                       f"username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"
