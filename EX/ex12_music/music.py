"""Music."""
from string import ascii_uppercase


class Note:
    """
    Note class.

    Every note has a name and a sharpness or alteration (supported values: "", "#", "b").
    """

    def __init__(self, note: str):
        """Initialize the class.

        To make the logic a bit easier it is recommended to normalize the notes, that is, choose a sharpness
        either '#' or 'b' and use it as the main, that means the notes will be either A, A#, B, B#, C etc. or
        A Bb, B, Cb, C.
        Note is a single alphabetical letter which is always uppercase.
        NB! Ab == Z#
        """
        self.original_note = note.capitalize()
        self.note = self.normalize_note(note)

    def normalize_note(self, note):
        """Normalize the note."""
        # Replace 'b' with '#' for consistency
        if len(note) > 1 and note[1].lower() == 'b':
            # Find the previous note
            prev_note = ascii_uppercase[ascii_uppercase.find(note[0].upper()) - 1]
            return prev_note + '#'
        return note.capitalize()

    def __repr__(self) -> str:
        """
        Representation of the Note class.

        Return: <Note: [note]> where [note] is the note_name + sharpness if the sharpness is given, that is not "".
        Repr should display the original note and sharpness, before normalization.
        """
        return f"<Note: {self.note[0].upper()}{self.note[1:]}>"

    def get_number(self):
        """Give the note a number."""
        if self.note == 'Ab':
            return 25.5
        pos = ascii_uppercase.find(self.note[0])
        if len(self.note) != 1:
            if self.note[1] == '#':
                pos += 0.5
            elif self.note[1].lower() == 'b':
                pos -= 0.5
        return pos

    def __hash__(self):
        """Hash the note."""
        return hash(self.get_number())

    def __eq__(self, other):
        """
        Compare two Notes.

        Return True if equal otherwise False. Used to check A# == Bb or Ab == Z#
        """
        if not isinstance(other, Note):
            return False
        if (self.note == 'Ab' and other.note == 'Z#') or (self.note == 'Z#' and other.note == 'Ab'):
            return True

        return self.get_number() == other.get_number()


class NoteCollection:
    """NoteCollection class."""

    def __init__(self):
        """
        Initialize the NoteCollection class.

        You will likely need to add something here, maybe a dict or a list?
        """
        self.notes = []

    def add(self, note: Note) -> None:
        """
        Add note to the collection.

        Check that the note is an instance of Note, if it is not, raise the built-in TypeError exception.

        :param note: Input object to add to the collection
        """
        if not isinstance(note, Note):
            raise TypeError
        elif note not in self.notes:
            self.notes.append(note)

    def pop(self, note: str) -> Note | None:
        """
        Remove and return previously added note from the collection by its name.

        If there are no elements with the given name, do not remove anything and return None.

        :param note: Note to remove
        :return: The removed Note object or None.
        """
        note_to_remove = Note(note)
        if note_to_remove in self.notes:
            return self.notes.pop(self.notes.index(note_to_remove))
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
        extracted_notes = self.notes.copy()
        self.notes = []
        return extracted_notes

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
        if not self.notes:
            return "Notes:\n  Empty."

        sorted_notes = sorted(self.notes, key=lambda x: x.note)
        content = "Notes:"
        for note in sorted_notes:
            content += f"\n  * {note.note}"
        return content


class Chord:
    """Chord class."""

    def __init__(self, note_one: Note, note_two: Note, chord_name: str, note_three: Note = None):
        """
        Initialize chord class.

        A chord consists of 2-3 notes and their chord product (string).
        If any of the parameters are the same, raise the 'DuplicateNoteNamesException' exception.
        """
        # Store the notes in a list, filtering out any None values (for optional third note).
        self.notes = [note for note in [note_one, note_two, note_three] if note is not None]
        # Extract and sort the original note names from the note objects.
        self.note_names = sorted(note.original_note for note in self.notes)
        # Create a set of unique note names for comparison.
        unique_name = set(self.note_names)
        # Check if the length of unique names is different from the total notes (indicating duplicates).
        length_not_matching = len(unique_name) != len(self.note_names)
        # Check if the chord name is not one of the note names.
        name_in_notes = all([name != chord_name for name in self.note_names])
        # Raise exception if there are duplicate note names or a note name matches the chord name.
        if length_not_matching or not name_in_notes:
            raise DuplicateNoteNamesException()

        # Set the chord name.
        self.chord_name = chord_name

    def __repr__(self) -> str:
        """
        Chord representation.

        Return as: <Chord: [chord_name]> where [chord_name] is the name of the chord.
        """
        return f"<Chord: {self.chord_name}>"


class Chords:
    """Chords class."""

    def __init__(self):
        """
        Initialize the Chords class.

        Add whatever you need to make this class function.
        """
        self.chords = []

    def add(self, chord: Chord) -> None:
        """
        Determine if chord is valid and then add it to chords.

        If there already exists a chord for the given pair of components, raise the 'ChordOverlapException' exception.

        :param chord: Chord to be added.
        """
        # Check for duplicate notes.
        for existing_chord in self.chords:
            if set(chord.notes) == set(existing_chord.notes):
                raise ChordOverlapException
        self.chords.append(chord)

    def get(self, first_note: Note, second_note: Note, third_note: Note = None) -> Chord | None:
        """
        Return the chord for the 2-3 notes.

        The order of the first_note and second_note and third_note is interchangeable.

        If there are no combinations for the 2-3 notes, return None

        Example:
          chords = Chords()
          chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
          print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
          print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
          print(chords.get(Note('D'), Note('Z')))  # ->  None
          chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
          print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

        :param first_note: The first note of the chord.
        :param second_note: The second note of the chord.
        :param third_note: The third note of the chord.
        :return: Chord or None.
        """
        notes_set = {first_note, second_note, third_note} if third_note else {first_note, second_note}
        for chord in self.chords:
            if notes_set == set(chord.notes):
                return chord
        return None


class DuplicateNoteNamesException(Exception):
    """Raised when attempting to add a chord that has same names for notes and product."""


class ChordOverlapException(Exception):
    """Raised when attempting to add a combination of notes that are already used for another existing chord."""


if __name__ == '__main__':
    chords = Chords()
    chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
    print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
    print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
    print(chords.get(Note('D'), Note('Z')))  # ->  None
    chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
    print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

    chords = Chords()

    chord1 = Chord(Note('A'), Note('C#'), 'Amaj', Note('E'))
    chord2 = Chord(Note('E'), Note('G'), 'Emin', note_three=Note('B'))
    chord3 = Chord(Note('E'), Note('B'), 'E5')

    chords.add(chord1)
    chords.add(chord2)
    chords.add(chord3)

    print(chords.get(Note('e'), Note('b')))  # -> <Chord: E5>

    try:
        wrong_chord = Chord(Note('E'), Note('A'), 'E')
        print('Did not raise, not working as intended.')
    except DuplicateNoteNamesException:
        print('Raised DuplicateNoteNamesException, working as intended!')

    try:
        chords.add(Chord(Note('E'), Note('B'), 'Emaj7add9'))
        print('Did not raise, not working as intended.')
    except ChordOverlapException:
        print('Raised ChordOverlapException, working as intended!')
