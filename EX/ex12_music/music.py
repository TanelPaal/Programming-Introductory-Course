"""Music."""
from string import ascii_uppercase

class Note:
    """
    Note class.

    Every note has a name and a sharpness or alteration (supported values: "", "#", "b").
    """
    note_equivalent = {'A#': 'Bb', 'Bb': 'A#',
                       'B#': 'Cb', 'Cb': 'B#',
                       'C#': 'Db', 'Db': 'C#',
                       'D#': 'Eb', 'Eb': 'D#',
                       'E#': 'Fb', 'Fb': 'E#',
                       'F#': 'Gb', 'Gb': 'F#',
                       'G#': 'Hb', 'Hb': 'G#',
                       'H#': 'Ib', 'Ib': 'H#',
                       'I#': 'Jb', 'Jb': 'I#',
                       'J#': 'Kb', 'Kb': 'J#',
                       'K#': 'Lb', 'Lb': 'K#',
                       'L#': 'Mb', 'Mb': 'L#',
                       'M#': 'Nb', 'Nb': 'M#',
                       'N#': 'Ob', 'Ob': 'N#',
                       'O#': 'Pb', 'Pb': 'O#',
                       'P#': 'Qb', 'Qb': 'P#',
                       'Q#': 'Rb', 'Rb': 'Q#',
                       'R#': 'Sb', 'Sb': 'R#',
                       'S#': 'Tb', 'Tb': 'S#',
                       'T#': 'Ub', 'Ub': 'T#',
                       'U#': 'Vb', 'Vb': 'U#',
                       'V#': 'Wb', 'Wb': 'V#',
                       'W#': 'Xb', 'Xb': 'W#',
                       'X#': 'Yb', 'Yb': 'X#',
                       'Y#': 'Zb', 'Zb': 'Y#',
                       'Z#': 'Ab', 'Ab': 'Z#',
                       'A': 'A',
                       'B': 'B',
                       'C': 'C',
                       'D': 'D',
                       'E': 'E',
                       'F': 'F',
                       'G': 'G',
                       'H': 'H',
                       'I': 'I',
                       'J': 'J',
                       'K': 'K',
                       'L': 'L',
                       'M': 'M',
                       'N': 'N',
                       'O': 'O',
                       'P': 'P',
                       'Q': 'Q',
                       'R': 'R',
                       'S': 'S',
                       'T': 'T',
                       'U': 'U',
                       'V': 'V',
                       'W': 'W',
                       'X': 'X',
                       'Y': 'Y',
                       'Z': 'Z'
                       }


    def __init__(self, note: str):
        """Initialize the class.

        To make the logic a bit easier it is recommended to normalize the notes, that is, choose a sharpness
        either '#' or 'b' and use it as the main, that means the notes will be either A, A#, B, B#, C etc or
        A Bb, B, Cb, C.
        Note is a single alphabetical letter which is always uppercase.
        NB! Ab == Z#
        """
        self.original_note = note
        self.note = note[0].upper()  # Normalizing to uppercase.

    def normalize_note(self, note: str) -> str:
        """
        Normalize the note.

        If the note is not in the note_equivalent dict, return the note as is.
        If the note is in the note_equivalent dict, return the equivalent note.
        """
        if note in self.note_equivalent:
            return self.note_equivalent[note]
        return note

    def __repr__(self) -> str:
        """
        Representation of the Note class.

        Return: <Note: [note]> where [note] is the note_name + sharpness if the sharpness is given, that is not "".
        Repr should display the original note and sharpness, before normalization.
        """
        return f"<Note: {self.original_note}>"

    def __eq__(self, other):
        """
        Compare two Notes.

        Return True if equal otherwise False. Used to check A# == Bb or Ab == Z#
        """
        if not isinstance(other, Note):
            return False
        if self.note == other.note:
            return True


class NoteCollection:
    """NoteCollection class."""


    def __init__(self):
        """
        Initialize the NoteCollection class.

        You will likely need to add something here, maybe a dict or a list?
        """


    def add(self, note: Note) -> None:
        """
        Add note to the collection.

        Check that the note is an instance of Note, if it is not, raise the built-in TypeError exception.

        :param note: Input object to add to the collection
        """

    def pop(self, note: str) -> Note | None:
        """
        Remove and return previously added note from the collection by its name.

        If there are no elements with the given name, do not remove anything and return None.

        :param note: Note to remove
        :return: The removed Note object or None.
        """
        return None

    def extract(self) -> list[Note]:
        """
        Return a list of all the notes from the collection and empty the collection itself.

        Order of the list must be the same as the order in which the notes were added.

        Example:
          collection = NoteCollection()
          collection.add(Note('A'))
          collection.add(Note('C'))
          collection.extract() # -> [<Note: A>, <Note: C>]
          collection.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted everything.

        :return: A list of all the notes that were previously in the collection.
        """
        return []

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the collection.

        Example:
          collection = NoteCollection()
          collection.add(Note('C#'))
          collection.add(Note('Lb'))
          print(collection.get_content())

        Output in console:
           Notes:
            * C#
            * Lb

        The notes must be sorted alphabetically by name and then by sharpness, that is A, A#, B, Cb, C and so on.
        Recommendation: Use normalized note names, not just the __repr__()

        :return: Content as a string
        """
        return ''

if __name__ == '__main__':
    note_one = Note('a') # yes, lowercase
    note_two = Note('C')
    note_three = Note('Eb')
    collection = NoteCollection()

    print(note_one) # <Note: A>
    print(note_three) # <Note: Eb>

    collection.add(note_one)
    collection.add(note_two)

    print(collection.get_content())
    # Notes:
    #   * A
    #   * C

    print(collection.extract()) # [<Note: A>,<Note: C>]
    print(collection.get_content())
    # Notes:
    #  Empty

    collection.add(note_one)
    collection.add(note_two)
    collection.add(note_three)

    print(collection.pop('a') == note_one)  # True
    print(collection.pop('Eb') == note_three)  # True