class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.likes = set()  # Like state initial
        self.matches = set()  #match state initial

    def like(self, other_user):
        self.likes.add(other_user.user_id)
        # Si l'autre utilisateur l'aime déjà, c'est un match
        if self.user_id in other_user.likes:
            self.matches.add(other_user.user_id)
            other_user.matches.add(self.user_id)
            print(f"It's a match between {self.name} and {other_user.name}!")

    def pass_user(self, other_user):
    
        pass


class TinderClone:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name)

    def user_like(self, user_id, other_user_id):
        user = self.users.get(user_id)
        other_user = self.users.get(other_user_id)
        if user and other_user:
            user.like(other_user)

    def user_pass(self, user_id, other_user_id):
        user = self.users.get(user_id)
        other_user = self.users.get(other_user_id)
        if user and other_user:
            user.pass_user(other_user)

    def get_matches(self, user_id):
        user = self.users.get(user_id)
        if user:
            return user.matches
        return set()


# Exemple d'utilisation
app = TinderClone()
app.add_user(1, 'Ablaye')
app.add_user(2, 'Rama')
app.add_user(3, 'Mame ')

# les utilisateur qui s'aime 
app.user_like(1, 2)
app.user_like(2, 1)
app.user_like(3, 1)
app.user_like(1, 3)

# Vérifiez les matches
print(f"Ablaye matches: {app.get_matches(1)}")
print(f"Rama matches: {app.get_matches(2)}")
print(f"Mame matches: {app.get_matches(3)}")
