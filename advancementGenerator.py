itemCondition = """
    "has_%s": {
      "conditions": {
        "items": [
          {
            "items": ["minecraft:%s"]
          }
        ]
      },
      "trigger": "minecraft:inventory_changed"
    }
"""

def generateAdvancement(recipeName, *itemNames):
    template = """{
  "parent": "vegan:recipes/root",
  "criteria": {
    %s
  },
  "requirements": [[%s]],
  "rewards": {
    "recipes": ["vegan:%s"]
  }
}
"""
    criteriaContent = ",\n".join([itemCondition % (x, x) for x in itemNames])
    requirements = ", ".join(['"has_%s"' % (x) for x in itemNames])
    return template % (criteriaContent, requirements, recipeName)


recipeName = "string"

f = open(recipeName + ".json", "w")
f.write(generateAdvancement(recipeName, "vine"))