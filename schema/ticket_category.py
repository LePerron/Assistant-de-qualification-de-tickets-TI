from enum import StrEnum


class TicketCategory(StrEnum):
    ACCESS = "Access"
    MANAGEMENT = "Management"
    APPLICATION = "Application"
    HARDWARE = "Hardware"
    NETWORK = "Network"
    SECURITY = "Security"
    ONBOARDING = "Onboarding"
    DATA = "Data"
    OTHER = "Other"
