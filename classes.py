import numpy as np

class Grid:
    def __init__(self, length, disp_decay, seed_ecol=1859, seed_biol=376, n_spawn=10):
        self.length = length
        self.disp_decay = disp_decay

        self.all_cells = []
        for i in range(self.length):
            for j in range(self.length):
                self.all_cells.append((i, j))

        # init ecol
        np.random.seed(1859)
        self.ecol = np.random.random((self.length, self.length))

        # init biol
        np.random.seed(1859)
        self.biol = np.zeros(self.ecol.shape)
        # spawn initial occurring spots
        for i in range(n_spawn):
            R = self.random_pos()
            self.biol[R[0], R[1]] = 1

        # init reproductive potential
        self.reproduction = np.full(self.ecol.shape, np.nan)

    def step(self, fitness_fxn, bernoulli=True):
        # calc reproductive potential per cell:  reproduction_ij = biol_ij*fitness(ecol_ij)
        for i, j in self.all_cells:
            self.reproduction[i, j] = self.biol[i, j] * fitness_fxn(self.ecol[i, j])

        # disperse
        # for each cell: add decayed reproductive potential to all cells (incl. self)
        biol_NEW = np.zeros(shape=self.biol.shape)
        # TODO: loop in parallel?
        for i, j in self.all_cells:
            for p, q in self.neighbours(i, j):  # considering only moore k-neighbours
                                                # => considerable speed up for larger grids
                biol_NEW[p, q] \
                    += self.reproduction[i, j] * 1 / np.power((1 + self.distance(i, j, p, q)), self.disp_decay)

        # update
        self.biol = np.clip(biol_NEW, a_min=0, a_max=1)
        if bernoulli:
            self.biol = np.random.binomial(1, self.biol)  # bernoulli sampling for stochastic component

        # To try: add other species. impose some restrictions on fitness distribution
        # To try: investigate population resilience under different modes of reproduction / resource landscape
        # e.g. orchids: have low dispersal decay, sparse landscape, with high temporal variation.
        # - perhaps interesting to see effect of perturbance on landscape plots / population
        # - try to demonstrate that strategy can evolve: e.g. trade-off of growth speed & dispersal-decay



    ### general auxiliary functions:

    def random_pos(self):
        return np.random.randint(self.length, size=2)

    def distance(self, i, j, p, q):
        return np.linalg.norm(np.array([i, j]) - np.array([p, q]))

    def neighbours(self, i, j, k=5):
        # for a large enough decay exponent: considering neighbors beyond 4 or 5 becomes ~negligible
        neigh = k  # moore neighbourhood
        i_low = np.clip(i - neigh, 0, self.length)
        i_high = np.clip(i + neigh + 1, 0, self.length)  # +1 bc range(a, b+1) -> a, .., b
        j_low = np.clip(j - neigh, 0, self.length)
        j_high = np.clip(j + neigh + 1, 0, self.length)
        neighbours = []
        for i_new in range(i_low, i_high):
            for j_new in range(j_low, j_high):
                neighbours.append((i_new, j_new))
        return neighbours
