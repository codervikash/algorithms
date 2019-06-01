"""
ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has to be moved far ahead, many movements are involved.

The idea of shellSort is to allow exchange of far items. In shellSort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. An array is said to be h-sorted if all sublists of every h’th element is sorted.

Time complexity:
        Best : O(n)
        Average : O((nlog(n))^2)
        Worst : O((nlog(n))^2)

Space complexity: O(1)

"""
