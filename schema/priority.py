from enum import StrEnum


# class Priority(Enum):
#     LOW = "demande standard, pas de blocage"
#     MEDIUM = "utilisateur bloqué ou petite équipe affectée"
#     High = "impact business important ou plusieurs utilisateurs affectés"
#     Critical = "panne majeure, sécurité, données sensibles, opérations arrêtées"

class TicketPriority(StrEnum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"
