from moysklad.api import MoySklad


sklad = MoySklad.get_instance('login', 'password')
client = sklad.get_client()
methods = sklad.get_methods()
