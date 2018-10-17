class CustomerSet:
    def __init__(self, customers=set()):
        self.customers = customers

class RequirementTree:
    def __init__(self, description='', children=set()):
        self.description = description
        self.children = children

    def leaves(self):
        leaves = set()
        
        if self.children == set():
            return {self}
        
        for child in self.children:
            leaves |= child.leaves()

        return leaves

class Qfd:
    def __init__(
            self,
            customers=CustomerSet(),
            requirements=RequirementTree()):
        self.customers = customers
        self.requirements = requirements

def main():
    customers = CustomerSet({'researchers', 'manufacturers'})
    requirements = RequirementTree('', {
        RequirementTree('manufacture the phantom', {
            RequirementTree('phantom design preparation', {
                RequirementTree('easy to obtain any specialized software'),
                RequirementTree('easy to use any specialized software')}),
            RequirementTree('phantom production', {
                RequirementTree('easy to obtain materials'),
                RequirementTree('inexpensive to obtain materials'),
                RequirementTree('easy to obtain necessary equipment')})}),
        RequirementTree('allow precise characterization of microstructure', {
            RequirementTree('tract identification'),
            RequirementTree('tract characterization', {
                RequirementTree(
                    'axon diameter distribution precisely measurable'),
                RequirementTree('axon density precisely measurable'),
                RequirementTree('axon orientation precisely measurable')})})})

    return Qfd(customers, requirements)

