import dataclasses
import random
from enum import Enum

from faker import Faker

faker = Faker("ru_RU")


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_year: str
    birth_month: str
    birth_day: str
    date_birthday: str
    subjects: list[str]
    hobbies: list[str]
    current_address: str
    state: str
    city: str
    picture: any


class Gender(Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class Hobbies(Enum):
    sports = "Sports"
    reading = "Reading"
    music = "Music"


class Subjects(Enum):
    arts = "Arts"
    biology = "Biology"
    hindi = "Hindi"
    english = "English"
    math = "Math"


class State(Enum):
    ncr = "NCR"
    uttar_pradesh = "Uttar Pradesh"
    haryana = "Haryana"
    rajasthan = "Rajasthan"


class City(Enum):
    #NCR
    delhi = "Delhi"
    gurgaon = "Gurgaon"
    noida = "Noida"
    #Uttar Pradesh
    agra = "Agra"
    lucknow = "Lucknow"
    merrut = "Merrut"
    #Haryana
    karnal = "Karnal"
    panipat = "Panipat"
    #Rajasthan
    jaipur = "Jaipur"
    jaiselmer = "Jaiselmer"


student = User(
    faker.first_name(),
    faker.last_name(),
    faker.email(),
    Gender.male.value,
    str(random.randint(1000000000, 9999999999)),
    "1995",
    "February",
    "21",
    "21 Feb 1995",
    [Subjects.biology.value, Subjects.arts.value],
    [Hobbies.music.value, Hobbies.sports.value, Hobbies.reading.value],
    faker.address(),
    State.ncr.value,
    City.gurgaon.value,
    "hubba_bubba.png"
)
