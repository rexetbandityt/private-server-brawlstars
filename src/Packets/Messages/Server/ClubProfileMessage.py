from Utils.Writer import Writer


class ClubProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24301
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeInt(0)
        self.writeInt(521)
        self.writeString("<cff2400>B<cff4800>@<cff6d00>M<cfe9100>D<cffb600>I<cffda00>T<cfffe00>M<cffff00>e<cdaff00>g<cb6ff00>a<c91ff00>T<c6dfe00>e<c48ff00>a</c> <c4>and</c> <cff002a>m<cff0054>h<cff007f>o<cff00a9>e<cff00d4>n<cfe00fe>i<cff00ff>x<cd400ff>F<caa00ff>i<c7f00ff>r<c5500ff>e</c>")
        self.writeVint(8)
        self.writeVint(11)
        self.writeVint(3)
        self.writeVint(1)
        self.writeVint(50000)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("IL")
        self.writeVint(0)
        self.writeString("Welcome!")
        self.writeVint(1)
        self.writeInt(3182494701)
        self.writeInt(2935259141)
        self.writeVint(7)
        self.writeString("<cff3200>M<cff6500>r<cff9800> <cffcb00>B<cffff00>@<cccff00>N<c99ff00>D<c66ff00>I<c33ff00>T<c01ff00>Bro</c>")
        self.writeVint(7)
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(60000)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(28)
        self.writeVint(33)
        self.writeVint(0)
        print("[INFO] Message ClubProfileMessage has been sent.")
