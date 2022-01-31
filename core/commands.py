class CreateJournalEntryCommand:
    def __init__(self, journal_entry_repo):
        self._repo = journal_entry_repo

    def run(self, author):
        return self._repo.create(author)
