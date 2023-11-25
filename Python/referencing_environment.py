class Symbol:
    def __init__(self):
        self.type = ""
        self.name = ""
        self.value = ""


#uses linked list
class SymbolTable:
    def __init__(self):
        self.symbols = [Symbol() for _ in range(MAX_SYMBOLS)]

#each node refers to a scope and contains a list of symbols within said scope
class Node:
    def __init__(self):
        self.symbolTable = SymbolTable()
        self.count = 0
        #implementation of the linked list here
        self.next = None
    #adds a new scope when we enter a block using linked list data structure
    def push_scope(self):
        new_node = Node()
        new_node.next = self
        return new_node
    #pops a new scope when we exit a block
    def pop_scope(self):
        if self is not None:
            self = self.next
            return self
        else:
            print("Cannot pop from an empty symbol table")
            return self

    def print_current_scope(self):
        if self is not None:
            print("Current Scope Symbols:")
            for i in range(self.count):
                print(f"{self.symbolTable.symbols[i].name}\t {self.symbolTable.symbols[i].value}")
            print("\n")
        else:
            print("Symbol table is empty")

    def print_all_scopes(self):
        current = self
        #iterating nodes (list of symbols in scope)
        while current is not None:
            print("Scope Symbols:")
            #print name value of ALL the symbols in a scope
            for i in range(current.count):
                print(f"{current.symbolTable.symbols[i].name}\t {current.symbolTable.symbols[i].value}")
            print("\n")
            current = current.next
            
    #inserts a variable into the symbol table
    def insert_symbol(self, symbol_type, symbol_name, symbol_value):
        if self.count < MAX_SYMBOLS:
            symbol = self.symbolTable.symbols[self.count]
            symbol.name = symbol_name
            symbol.value = symbol_value
            symbol.type = symbol_type
            self.count += 1
        else:
            print("Symbol table is full")
        
    #checks if symbol exists in all scopes
    def symbol_exists(self, name):
        current = self
        while current is not None:
            for i in range(current.count):
                if current.symbolTable.symbols[i].name == name:
                    return current.symbolTable.symbols[i]
            current = current.next
        return None
    
    #checks if symbol exists in the current scope
    def symbol_existsInCurrent(self, name):
        current = self
        for i in range(current.count):
            if current.symbolTable.symbols[i].name == name:
                return current.symbolTable.symbols[i]
        return None
#sets the head
def free_environment(head):
    while head is not None:
        temp = head
        head = head.next
        del temp


MAX_SYMBOLS = 100

