from functools import wraps


# class FileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()
#         if exc_type:
#             print('vla', exc_val)
#
#
# with FileManager('test.txt', 'w') as f:
#     f.write('I am gonna writw something')


# def get_current_user_role():
#     return 'guest'
#
#
# def authorize(required_role):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(self, *args, **kwargs):
#             user_role = get_current_user_role()
#             if user_role != required_role:
#                 print('Access denied')
#                 return None
#             return func(self, *args, **kwargs)
#
#         return wrapper
#     return decorator
#
#
# class App:
#     @authorize(['admin', 'guest'])
#     def admin_dashboard(self):
#         print('Access given for admin dash')
#
#     @authorize('guest')
#     def guest_dashboard(self):
#         print('Access given for guest dash')
#
#
# app = App()
# app.admin_dashboard()
# app.guest_dashboard()