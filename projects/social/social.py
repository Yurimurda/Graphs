import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0       
        self.users = {}     
        self.friendships = {} # adjacency list

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(User)

        # Create friendships
        # if 1 is a friend of 2 and 2 is a friend of 1, count this as 2 friendships
        potential_friendships = avg_friendships * num_users

        # create a list with all possible friendship combinations
        # friendship_combos = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        friendship_combos = []

        # shuffle this list, then grab first N elements from the list. Import random.
        for user_id in range(1, num_users + 1):
            for friend_id in range(user_id + 1, num_users + 1):
                friendship_combos.append((user_id, friend_id))


        self.fisher_yates_shuffle(friendship_combos)

        friendships_to_make = friendship_combos[:(potential_friendships // 2)]

        for friendship in friendships_to_make:
            self.add_friendship(friendship[0], friendship[1])
        
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        queue = Queue()

        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue.enqueue([user_id])

        while queue.size() > 0:

            current_path = queue.dequeue()

            current_vertex = current_path[-1]
            if current_vertex not in visited:



                visited[current_vertex] = current_path

                for neighbor in self.friendships[current_vertex]:
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
