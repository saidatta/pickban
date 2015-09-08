import decimal, math

class Team:
    champDict = {}

    def addChampionBan(self, team, cPicked):
        if (team not in self.champDict):
            self.champDict[team] = []
            self.champDict[team].append({"champion" : cPicked, "picked": 1})
        else:
            if(len(self.searchChampion(cPicked, self.champDict[team])) == 0):
                self.champDict[team].append({ "champion": cPicked, "picked": 1})
            else:
                self.searchChampion(cPicked, self.champDict[team])[0]["picked"] += 1

    def searchChampion(self, name, people):
        return [element for element in people if element['champion'] == name]

    def getChampPickPercentage(self, team, isDecimalAllowed):
        champPickPercentages = {}
        teamPicked = self.champDict[team];
        totalSum = self.getTotalChampPicked(team)
        for championInfo in teamPicked:
            if(isDecimalAllowed):
                champPickPercentages[championInfo["champion"]] = round(decimal.Decimal((championInfo["picked"]/totalSum) * 100), 2)
            else:
                champPickPercentages[championInfo["champion"]] = math.ceil((championInfo["picked"]/totalSum) * 100)
        return champPickPercentages

    def getTotalChampPicked(self, team):
        teamPicked = self.champDict[team];
        totalSum = 0
        for championInfo in teamPicked:
            totalSum += championInfo["picked"]
        return totalSum;

def main():
    print("Welcome to champ ban percentages")
    tP = Team()
    tP.addChampionBan("KTR", "GangPlank")
    tP.addChampionBan("KTR", "Ashe")
    tP.addChampionBan("KTR", "Kalista")
    tP.addChampionBan("JAG", "Shen")
    tP.addChampionBan("JAG", "Fizz")
    tP.addChampionBan("JAG", "Lulu")
    tP.addChampionBan("KTR", "Gangplank")
    tP.addChampionBan("KTR", "Kalista")
    tP.addChampionBan("KTR", "Viktor")
    tP.addChampionBan("JAG", "Shen")
    tP.addChampionBan("JAG", "Fizz")
    tP.addChampionBan("JAG", "Fiora")
    tP.addChampionBan("JAG", "Shen")
    tP.addChampionBan("JAG", "Azir")
    tP.addChampionBan("JAG", "Lulu")
    tP.addChampionBan("KTR", "Gangplank")
    tP.addChampionBan("KTR", "Ashe")
    tP.addChampionBan("KTR", "Elise")
    tP.addChampionBan("KTR", "Gangplank")
    tP.addChampionBan("KTR", "Twisted Fate")
    tP.addChampionBan("KTR", "Kalsita")
    tP.addChampionBan("JAG", "Shen")
    tP.addChampionBan("JAG", "Azir")
    tP.addChampionBan("JAG", "Lulu")
    print(tP.getChampPickPercentage("JAG",False))
    print(tP.getChampPickPercentage("KTR", False))

main()