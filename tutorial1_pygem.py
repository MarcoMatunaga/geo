from pygem import FFDParameters, FFD, StlHandler
params = FFDParameters()
params.read_parameters(
    filename='PyGem/tests/test_datasets/parameters_test_ffd_sphere.prm')
stl_handler = StlHandler()
mesh_points = stl_handler.parse('PyGem/tests/test_datasets/test_sphere.stl')
fig = stl_handler.plot(plot_file='PyGem/tests/test_datasets/test_sphere.stl')
free_form = FFD(params, mesh_points)
free_form.perform()
new_mesh_points = free_form.modified_mesh_points
stl_handler.write(new_mesh_points, 'test_sphere_mod.stl')
fig = stl_handler.plot(plot_file='test_sphere_mod.stl')
