from repository.repository import Repository
from service.admin_service import AdminService
from service.client_service import ClientService
from ui.console import UI

repository = Repository()

admin_service = AdminService(repository)
client_service = ClientService(repository)

ui = UI(admin_service, client_service)

ui.run()