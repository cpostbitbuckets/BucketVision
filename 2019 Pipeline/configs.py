configs = {
	'camera_res': (320, 240),
	'crop_top': 2/6,
	'crop_bot': 5/6,
	'brigtness': 3
}
cropped_vres = int(configs['camera_res'][1]*(configs['crop_bot'])) - int(configs['camera_res'][1]*(configs['crop_top']))
configs['output_res'] = (configs['camera_res'][0], cropped_vres)


