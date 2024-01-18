import tkinter as tk

class TowerOfHanoi:
    def __init__(self, root):
        self.root = root
        self.root.title("Tour d'Hanoï")

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.disks = 3  # Nombre de disques (modifiable)
        self.towers = [[], [], []]  # Piles représentant les tours

        # Initialisation des tours
        for i in range(self.disks, 0, -1):
            disk_width = i * 30
            self.towers[0].append(self.canvas.create_rectangle(300 - disk_width // 2, 380 - 20 * i,
                                                               300 + disk_width // 2, 400 - 20 * i, fill='blue'))

        self.selected_disk = None
        self.selected_tower = None
        self.canvas.bind("<Button-1>", self.select_disk)

    def select_disk(self, event):
        x, y = event.x, event.y
        for tower_index, tower in enumerate(self.towers):
            for disk_index, disk in enumerate(tower):
                if self.canvas.coords(disk)[0] <= x <= self.canvas.coords(disk)[2] and \
                        self.canvas.coords(disk)[1] <= y <= self.canvas.coords(disk)[3]:
                    if self.selected_disk is None:
                        self.selected_disk = disk
                        self.selected_tower = tower_index
                    else:
                        if self.selected_disk != disk:
                            if self.is_valid_move(self.selected_tower, tower_index):
                                self.move_disk(self.selected_tower, tower_index)
                        self.selected_disk = None
                    return

    def is_valid_move(self, from_tower, to_tower):
        if len(self.towers[to_tower]) == 0:
            return True
        elif self.canvas.coords(self.towers[from_tower][-1])[2] <= self.canvas.coords(self.towers[to_tower][-1])[0]:
            return True
        return False

    def move_disk(self, from_tower, to_tower):
        disk = self.towers[from_tower].pop()
        x_diff = self.canvas.coords(self.towers[to_tower][-1])[2] - self.canvas.coords(disk)[2]
        y_diff = self.canvas.coords(self.towers[to_tower][-1])[3] - self.canvas.coords(disk)[3]
        self.canvas.move(disk, x_diff, y_diff)
        self.towers[to_tower].append(disk)

def main():
    root = tk.Tk()
    app = TowerOfHanoi(root)
    root.mainloop()

if __name__ == "__main__":
    main()
