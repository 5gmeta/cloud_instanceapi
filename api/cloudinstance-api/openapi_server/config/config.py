import connexion

# Create the Connexion application instance
connexion_app = connexion.App(__name__, specification_dir='../openapi/')
app = connexion_app.app
