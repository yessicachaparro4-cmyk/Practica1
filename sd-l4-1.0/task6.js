export class Player {
    constructor(name, level) {
        this.name = name;
        this.level = level;
        this.party = [];
    }

    info() {
        return this.name + " has reached Level " + this.level + "!";
    }

    levelUp() {
        this.level++;
    }

    addToParty(player) {
        this.party.push(player);
    }

    removeFromParty(player) {
        const index = this.party.indexOf(player);

        if (index !== -1) {
            this.party.splice(index, 1);
        }
    }
}