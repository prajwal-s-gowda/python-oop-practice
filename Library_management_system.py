class Playlist:
    def __init__(self,songs):
        self.songs=songs

    def __len__(self):
        return len(self.songs)

l1=Playlist(["songA","songB","songC","songD"])
print(len(l1))
