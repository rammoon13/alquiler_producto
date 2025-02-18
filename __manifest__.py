# alquiler_productos/__manifest__.py
{
    'name': 'Gestión de Alquiler de Productos',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Gestión del servicio de alquiler de productos.',
    'description': """
        Módulo para gestionar el alquiler de productos a clientes.
        Permite registrar préstamos, controlar la disponibilidad
        y gestionar el estado de los productos alquilados.
    """,
    'author': 'Ramon Herrera',
    'depends': ['base', 'sale', 'contacts', 'product'], # Requiere módulos base, ventas, contactos y productos
    'data': [
        'views/alquiler_producto_views.xml',
        'security/ir.model.access.csv',
        'data/cron_jobs.xml'
    ],
    'icon': '/alquiler_producto/static/description/icon56.png',
    'installable': True,
    'application': True,
}
