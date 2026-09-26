export class Player {
    constructor(name, level) {
        this.name = name;
        this.level = level;
        this.xp = 0;
    }

    info() {
        return this.name + " has reached Level " + this.level + "!";
    }

    levelUp() {
        this.level++;
    }

    gainXP(points) {
        this.xp += points;

        if (this.xp >= 100) {
            this.levelUp();
            this.xp -= 100;
        }
    }
}