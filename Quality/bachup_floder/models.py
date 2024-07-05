""" Models """
from datetime import datetime
from flask_login import UserMixin
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from Quality import db, login_manager,app




@login_manager.user_loader
def load_user(user_id):
    """Standard user loader function from Flask-Login documentation"""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """User class"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.now)
    last_login = db.Column(db.DateTime, default=datetime.now)
    tasks = db.relationship('Task', backref='user', lazy=True)


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token,expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token,max_age=expires_sec)['user_id']
        except Exception:
            return None
        return User.query.get(user_id)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class NonConformity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_detection = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    origine = db.Column(db.String(100), nullable=False)
    etape_detection = db.Column(db.String(100), nullable=False)
    declencheur = db.Column(db.String(100), nullable=False)
    provenance = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    version_formule = db.Column(db.String(50), nullable=False)
    code_mp = db.Column(db.String(50), nullable=False)
    n_lot = db.Column(db.String(50), nullable=False)
    dte_h_production = db.Column(db.DateTime, nullable=False)
    dte_h_chargement = db.Column(db.DateTime, nullable=False)
    enlevement = db.Column(db.String(100), nullable=False)
    transporteur = db.Column(db.String(100), nullable=False)
    matricule = db.Column(db.String(50), nullable=False)
    qte_commandee = db.Column(db.Float, nullable=False)
    qte_livree = db.Column(db.Float, nullable=False)
    qte_concernee = db.Column(db.Float, nullable=False)
    qte_retour = db.Column(db.Float, nullable=False)
    lieu_stockage = db.Column(db.String(100), nullable=False)
    equipement = db.Column(db.String(100), nullable=False)
    motif = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    decision = db.Column(db.String(100), nullable=False)
    criticite = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(20), nullable=True)
    commentaire = db.Column(db.Text, nullable=True)
    statut_nc = db.Column(db.String(50), nullable=False, default='open')
    date_statut = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    necessite_traitement = db.Column(db.Boolean, nullable=False, default=True)
    reported_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cause_analysis = db.relationship('CauseAnalysis', backref='nonconformity', uselist=False)
    action_plan = db.relationship('ActionPlan', backref='nonconformity', uselist=False)

class CauseAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    analysis = db.Column(db.Text, nullable=False)
    non_conformity_id = db.Column(db.Integer, db.ForeignKey('non_conformity.id'), nullable=False)


class ActionPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_action = db.Column(db.String(100), nullable=False)
    action = db.Column(db.Text, nullable=False)
    critere_evaluation = db.Column(db.String(100), nullable=False)
    pilote = db.Column(db.String(100), nullable=False)
    date_echeance = db.Column(db.DateTime, nullable=False)
    date_realisation = db.Column(db.DateTime, nullable=True)
    statut = db.Column(db.String(50), nullable=False)
    efficacite = db.Column(db.String(50), nullable=True)
    non_conformity_id = db.Column(db.Integer, db.ForeignKey('non_conformity.id'), nullable=False)
