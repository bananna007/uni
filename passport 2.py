from datetime import date, datetime

class Passport:
    """Digital passport with ID and travel records."""

    _passport_id_counter = 0
    def __init__(self, first_name, last_name, dob, country, exp_date):
        """Sets up passport with holder info."""
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        self.country = country
        self.exp_date = datetime.strptime(exp_date, "%Y-%m-%d").date()
        self._countries_visited = {}
        self._passport_id = Passport._passport_id_counter
        Passport._passport_id_counter += 1

    def summary(self):
        """Returns passport summary as a string."""
        status = "valid" if self.is_valid() else "invalid"
        return (f"This passport belongs to {self.first_name} {self.last_name}, born on {self.dob} "
                f"in The {self.country}. It is {status}.")

    def is_valid(self):
        """Checks if passport is valid."""
        return self.exp_date > date.today()

    def check_data(self, first_name, last_name, dob, country):
        """Checks if given info matches and passport is valid."""
        return (self.first_name == first_name and
                self.last_name == last_name and
                self.dob == datetime.strptime(dob, "%Y-%m-%d").date() and
                self.country == country and
                self.is_valid())

    def stamp(self, country):
        """Records a visit if it's not the home country."""
        if country != self.country:
            if country in self._countries_visited:
                self._countries_visited[country] += 1
            else:
                self._countries_visited[country] = 1

    def countries_visited(self):
        """Lists all countries visited."""
        return self._countries_visited.keys()

    def times_visited(self, country):
        """Returns how many times a country was visited."""
        return self._countries_visited.get(country, 0)

    def sum_square_visits(self):
        """Calculates sum of squares of visit counts."""
        return sum(count ** 2 for count in self._countries_visited.values())

    def passport_number(self):
        """Gets passport ID number."""
        return self._passport_id

if __name__ == "__main__":
    alan = Passport("Alan", "Turing", "1912-06-23", "The United Kingdom", "1954-06-07")
    print("Alan is valid:", alan.is_valid())
    print(alan.summary())

    codegrade = Passport("Code", "Grade", "2017-07-21", "The Netherlands", "2999-12-31")
    print(codegrade.check_data("Code", "Grade", "2017-07-21", "The Netherlands"))

    codegrade.stamp("France")
    codegrade.stamp("France")
    codegrade.stamp("Germany")
    print("Countries visited:", list(codegrade.countries_visited()))
    print("Times visited France:", codegrade.times_visited("France"))
    print("Sum square visits:", codegrade.sum_square_visits())


