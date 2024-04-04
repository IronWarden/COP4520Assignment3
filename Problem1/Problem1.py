import threading
import random

class Present:
    def __init__(self, tag):
        self.tag = tag
        self.next = None
        self.lock = threading.Lock()

class ChainOfPresents:
    def __init__(self):
        self.lock = threading.Lock()
        self.head = None
        self.set = set() # shared set to tell which tags were already processed 
    # add a present to the chain 
    def add_present(self, tag):
        present = Present(tag)
        self.set.add(tag)
        if tag not in self.set:
            if not self.head or self.head.tag > tag:
                present.next = self.head
                self.head = present
                return
            current = self.head
            while current.next and current.next.tag < tag:
                current = current.next

            present.next = current.next
            current.next = present
    # method to thank guest by removing them from the chain 
    def thankGuest(self, tag):
        if tag in self.set:
            self.set.remove(tag) # remove it from shared set 
            if not self.head:
                return 
            if self.head.tag == tag:
                self.head = self.head.next
                return 
            current = self.head

            while current.next:
                if current.next.tag == tag:
                    current.next = current.next.next
                    return
                current = current.next
    # method to search a present in the chain by tag
    def search(self, tag):
 
        with self.lock:
            current = self.head
            while current:
                    if current.tag == tag:
                        print(f'Tag #{tag} found as requested by minotaur')
                    current = current.next
            

def task(presents, chain_of_presents):
    # alternate betweeen adding and thankign the guest with minotaur requesting a search 
    alternate = True
    for present in presents:
        choice = random.randint(1, 5) # minotaur may decide any servant to search a present

        if choice == 1:
            chain_of_presents.search(present)
        elif alternate:
            chain_of_presents.add_present(present)
            alternate = False
        elif not alternate:
            chain_of_presents.thankGuest(present)
            alternate = True

def main():
    num_presents = 500000
    chain_of_presents = ChainOfPresents()
    servants = 4
    threads = []
    unordered_presents = random.sample(
        range(1, num_presents + 1), num_presents)

    for i in range(servants):
        start_idx = i * (len(unordered_presents) // servants)
        end_idx = (i + 1) * (len(unordered_presents) // servants)
        servant_presents = unordered_presents[start_idx:end_idx]
        thread = threading.Thread(target=task, args=(
            servant_presents, chain_of_presents))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
   
    if chain_of_presents.head is None:
        print("All thank yous have been written")
    else:
        current = chain_of_presents.head
        count = 0
        while current.next is not None:
            count += 1
            current = current.next
        print(f'There are {count} guests not thanked')

if __name__ == "__main__":
    main()