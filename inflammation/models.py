"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


class Patient:
    def __init__(self, name, observations=None):
        self.name = name

        if observations is None:
            self.observations = []

        else:
            self.observations = observations

    def add_observation(self, obs):
        self.observations.append(obs)


class Doctor:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def write_patient(self, patient_name):
        new_patient = Patient(patient_name)

        self.patients.append(new_patient.name)
        return new_patient


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array."""
    return np.min(data, axis=0)


alice = Patient('Alice')
print(alice)

denis = Doctor('Doc. Denis')
denis.write_patient('Alice')
denis.write_patient('Roberta')
denis.write_patient('Lucas')

print(denis.patients)

# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
