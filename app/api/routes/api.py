from flask import Blueprint, request, jsonify, session
from app.api.models import Client, Contact, Country 
from app.api.db import get_db
import json
from sqlalchemy import inspect

bp = Blueprint('/api', __name__, url_prefix='/api')

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


@bp.route('/clients')
def showClients():
    db = get_db()
    clients = (
     db.query(Client)
     .all()
        
    )
    print([object_as_dict(r) for r in clients])
    
    
    return json.dumps([object_as_dict(r) for r in clients])



