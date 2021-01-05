# least common ancestor : 최소 공통 조상
# 트리에서 가장 가까이 있는 공통된 조상을 찾는 알고리즘
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
data_array = {
    '병원': ['관리부'],
    '관리부': ['물류팀', '행정팀', '미화팀'],
    '물류팀': ['전자기기', 'A업체'],
    '행정팀': ['행정실'],
    '미화팀': ['B업체', 'C업체', 'D업체'],
    '전자기기': ['창고1'],
    'A업체': ['창고2', '창고3', '창고4', '분류실'],
    '행정실': [],
    'B업체': ['A병동'],
    'C업체': ['B병동, C병동'],
    'D업체': ['창고6'],
    '창고1': [],
    '창고2': [],
    '창고3': [],
    '창고4': ['보관실', '운반실'],
    '분류실': [],
    'A병동': ['102'],
    'B병동': ['응급실', '200'],
    'C병동': ['300'],
    '창고6': [],
    '보관실': [],
    '운반실': ['창고5'],
    '102': [],
    '응급실': [],
    '200': [],
    '300': [],
    '창고5': []
}
keys = list(data_array)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def __str__(self):
        return self.data


class Tree:
    def __init__(self):
        self.root = TreeNode('병원')
        self.node_list = []
        self.room_list = []
        self.node_list.append(self.root)
        self.room_list.append('병원')

    def add_node(self, data):
        if data not in self.room_list:
            self.room_list.append(data)
            self.node_list.append(TreeNode(data))

    def find_node(self, string):
        for node in self.node_list:
            if node.data == string:
                return node
        return False

    def define_relationship(self, data_dict):
        # 자식 관계 설정
        for key in keys:
            for item in data_dict.get(key):
                if item != None:
                    self.find_node(key).children.append(self.find_node(item))
                    if self.find_node(item) != False:
                        self.find_node(item).parent = self.find_node(key)


org_chart = Tree()
# 트리에 데이터 추가
for key in keys:
    org_chart.add_node(key)
org_chart.define_relationship(data_array)


# 학습자 구현 부분
def lsa(tree, a, b):
    a_node = tree.find_node(a)
    b_node = tree.find_node(b)
    a_parent = []
    b_parent = []

    if a_node and b_node:
        while(a_node):
            a_parent.append(a_node.data)
            a_node = a_node.parent

        while(b_node):
            b_parent.append(b_node.data)
            b_node = b_node.parent

        print(a_parent)
        print(b_parent)

    for a in a_parent:
        for b in b_parent:
            if a == b:
                return(a)


print(lsa(org_chart, '창고5', '분류실'))
