from flask import Blueprint

routes = Blueprint('routes', __name__)

from .player import *
from .quest import *
from .leaderboard import *