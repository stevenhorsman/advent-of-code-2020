import allergen_assessment, fileinput

def test_part1_example_1():
  data = '''
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''[1:]
  assert allergen_assessment.part1(data) == 5

def test_part1():
  with open(allergen_assessment.input_file) as f:
    data = f.read()
  expected = 2436
  assert allergen_assessment.part1(data) == expected

def test_part2_example_1():
  data = '''
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''[1:]
  assert allergen_assessment.part2(data) == 'mxmxvkd,sqjhc,fvjkl'

def test_part2():
  with open(allergen_assessment.input_file) as f:
    data = f.read()
  expected = 'dhfng,pgblcd,xhkdc,ghlzj,dstct,nqbnmzx,ntggc,znrzgs'
  assert allergen_assessment.part2(data) == expected
