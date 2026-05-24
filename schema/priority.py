from enum import Enum


class Priority(Enum):
    LOW = "demande standard, pas de blocage"
    MEDIUM = "utilisateur bloqué ou petite équipe affectée"
    High = "impact business important ou plusieurs utilisateurs affectés"
    Critical = "panne majeure, sécurité, données sensibles, opérations arrêtées"
