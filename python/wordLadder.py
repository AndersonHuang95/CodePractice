import collections 

class Solution(object):

    # Solution using double BFS

    def findLadders(self, begin, end, words_list):
        
        def construct_paths(source, dest, tree):
            if source == dest: 
                return [[source]]
            return [[source] + path for succ in tree[source]
                                    for path in construct_paths(succ, dest, tree)]

        def add_path(tree, word, neigh, is_forw):
            if is_forw: tree[word]  += neigh,
            else:       tree[neigh] += word,

        def bfs_level(this_lev, oth_lev, tree, is_forw, words_set):
            if not this_lev: return False
            if len(this_lev) > len(oth_lev):
                return bfs_level(oth_lev, this_lev, tree, not is_forw, words_set)
            for word in (this_lev | oth_lev):
                words_set.discard(word)
            next_lev, done = set(), False
            while this_lev:
                word = this_lev.pop()
                for c in "abcdefghijklmnopqrstuvwxyz":
                    for index in range(len(word)):
                        neigh = word[:index] + c + word[index+1:]
                        if neigh in oth_lev:
                            done = True
                            add_path(tree, word, neigh, is_forw)                
                        if not done and neigh in words_set:
                            next_lev.add(neigh)
                            add_path(tree, word, neigh, is_forw)
            return done or bfs_level(next_lev, oth_lev, tree, is_forw, words_set)
        
        words_list = set(words_list)                   
        tree, path, paths = collections.defaultdict(list), [begin], []
        is_found = bfs_level(set([begin]), set([end]), tree, True, words_list)
        return construct_paths(begin, end, tree)

    def findLadders(self, begin_word, end_word, words_list): 
        """
        Bidirectional BFS will speed up this code 
        Use a tree to store edges in graph build-up
        Use a set structure to act as queue, we need this to gain constant time access to 
        any element currently on the frontier (forward or backward)

        Args: 
            begin_word (str):
            end_word (str):
            word_list (List[str]):
        Returns: 
            List[List[str]]: 
        """

        def construct_paths(source, dest, graph):
            if source == dest: 
                return [[source]]
            return [[source] + path for succ in graph[source]
                                    for path in construct_paths(succ, dest, graph)]

        def bfs(front, back, graph, words_set): 
            """
            Perform bidirectional BFS on a dictionary of words

            Args:
                front (set(str)):
                back (set(str)):
                graph (defaultdict(list)): 
                words_set (set(str)): 
            Returns:
            """
            while front and back: 
                # --- prevent cycling by removing used words --- 
                for word in (front | back): 
                    words_set.discard(word)

                next_front = set()
                while front: 
                    current = front.pop()
                    next_front |= word_search(current, graph, front, back, words_set)
                front = next_front

                next_back = set()
                while back: 
                    current = back.pop()
                    next_back |= word_search(current, graph, back, front, words_set)
                back = next_back

        def word_search(word, graph, front, back, words_set): 
            nxt = set()
            done = False
            for index in range(len(word)): 
                for c in "abcdefghijklmnopqrstuvwxyz":
                    neighbor = word[:index] + c + word[index + 1:]
                    if neighbor in back: 
                        done = True
                        graph[word] += neighbor
                    if not done and neighbor in words_set: 
                        nxt.add(neighbor)
                        graph[word] += neighbor
            return nxt

        words_set = set(words_list)
        graph, ans = collections.defaultdict(list), []
        front, back = set([begin_word]), set([end_word])
        bfs(front, back, graph, words_set)
        return construct_paths(begin_word, end_word, graph)

sol = Solution()
print(sol.findLadders('red', 'tax', ["ted","tex","red","tax","tad","den","rex","pee"]))