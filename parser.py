import os
import sys

scr_file_name = "string"
scr_file = "file_string"
scripts = "./Scripts-pt/"
actual_bg = "000.jpg"
previours_command = "A_"
type_loaded = "N"
cmd_path = './Commands-pt/'
prev_c_ld = None
prev_l_ld = None
prev_r_ld = None
c_typeis_loaded = False
l_typeis_loaded = False
r_typeis_loaded = False

if len(sys.argv) >= 2:
    if os.path.isfile(sys.argv[1]) == True and os.path.exists(sys.argv[1]) == True:
        
        result_file = open(sys.argv[1],encoding='latin-1')
        lines = result_file.readlines()

        for line in lines:
            
            if line.startswith(';') == True:
                pass
            elif line.startswith('*s') == True or line.startswith('*eclipse') == True or line.startswith('*opening') == True: 
                if line.endswith('*') == False and line.startswith("*skip") == False:
                    scr_file_name = line.strip()[1:]
                    print(scripts + scr_file_name + ".scr")
                
                    if os.path.isfile(scripts + scr_file_name + ".scr") == True and os.path.exists(scripts + scr_file_name + ".scr") == True:
                        scr_file = open(scripts + scr_file_name + ".scr",encoding='latin-1',mode='a')
                
                    else:
                        actual_bg = "000.jpg"
                        type_loaded = "N"
                        r_typeis_loaded = False
                        l_typeis_loaded = False
                        c_typeis_loaded = False

                        prev_c_ld = None
                        prev_l_ld = None
                        prev_r_ld = None
                        scr_file = open(scripts + scr_file_name + ".scr",encoding='latin-1',mode='w')
            
            elif os.path.exists(scripts + scr_file_name + ".scr") == True:

                if line.startswith('`') == True:
                    corrected_line = line.replace("\\", '').replace('` ',"text ").replace('`', "text ").replace('@ ', '\ntext ').replace('|', '..').replace('@','')
                    if corrected_line != "\ntext":
                        scr_file.write(corrected_line)
                
                elif line.startswith("waveloop "):
                    asset_in_line = line[len("waveloop "):].replace("se", "SE_")
                    asset_prefix = asset_in_line[:3]
                    new_index = int(asset_in_line[3:])+1
                    corrected_line = f"sound {asset_prefix}{new_index}.ogg -1\n"
                    previours_command = corrected_line
                    scr_file.write(corrected_line)
                
                elif line.startswith("bg "):
                    asset_in_line = line.replace('"','')
                    
                    if asset_in_line.startswith('bg image\\event\\'):
                        asset_in_line = line.replace('"','').replace('bg image\\event\\','').split(",")[0]
                        asset_prefix = asset_in_line.split(".")[0].upper()
                        asset_format = asset_in_line[-3:].replace('"','')
                        corrected_line = f"bgload event/{asset_prefix}.{asset_format}\n"
                        actual_bg = corrected_line
                        previours_command = corrected_line
                        scr_file.write(corrected_line)
                    
                    elif asset_in_line.startswith('bg image\\bg\\'):
                        asset_in_line = line.replace('"','').replace('bg image\\bg\\','').split(",")[0]
                        asset_prefix = asset_in_line.split(".")[0].upper()
                        asset_format = asset_in_line[-3:]
                        corrected_line = f"bgload {asset_prefix}.{asset_format}\n"
                        actual_bg = corrected_line
                        previours_command = corrected_line
                        scr_file.write(corrected_line)
                    
                    elif asset_in_line.startswith('bg image\\word\\'):
                        asset_in_line = line.replace('"','').replace('bg image\\word\\','').split(",")[0]
                        asset_prefix = asset_in_line.split(".")[0].upper()
                        asset_format = asset_in_line[-3:]
                        corrected_line = f"bgload {asset_prefix}.{asset_format}\n"
                        actual_bg = corrected_line
                        previours_command = corrected_line
                        scr_file.write(corrected_line)
                
                elif line.startswith("wavestop"):
                    corrected_line = line.replace("wavestop", "sound ~")
                    previours_command = corrected_line
                    scr_file.write(corrected_line)
                
                elif line.startswith("play "):
                    asset_in_line = line[len("play "):].replace('*','0').replace('"','').replace('\n','')
                    corrected_line = "music "+ asset_in_line + ".mp3\n"
                    previours_command = corrected_line
                    scr_file.write(corrected_line)
                
                elif line.startswith("playstop"):
                    corrected_line = line.replace("playstop\n", "music ~\n")
                    previours_command = corrected_line
                    scr_file.write(corrected_line)
                
                elif line.startswith("ld "):
                    asset_prefix = "empty"
                    print(line)
                    if line.startswith("ld c"):
                        if c_typeis_loaded == True or type_loaded == 'c':
                            scr_file.write(actual_bg)
                            if r_typeis_loaded == True:
                                scr_file.write(prev_r_ld)
                            if l_typeis_loaded == True:
                                scr_file.write(prev_l_ld)                        
                        asset_prefix = line.replace('"','').replace('ld c,:a;image\\tachi\\','').replace('.jpg,','').replace('.png,','')
                        c_typeis_loaded = True
                        type_loaded = 'c'
                    
                    elif line.startswith("ld l"):
                        if l_typeis_loaded == True or type_loaded == 'l':
                            scr_file.write(actual_bg)
                            if r_typeis_loaded == True:
                                scr_file.write(prev_r_ld)
                            if c_typeis_loaded == True:
                                scr_file.write(prev_c_ld)
                        asset_prefix = line.replace('"','').replace('ld l,:a;image\\tachi\\','').replace('.jpg,','').replace('.png,','')
                        l_typeis_loaded = True
                        type_loaded = 'l'
                    
                    elif line.startswith("ld r"):
                        if r_typeis_loaded == True or type_loaded == 'r':
                            scr_file.write(actual_bg)
                            if l_typeis_loaded == True:
                                scr_file.write(prev_l_ld)
                            if c_typeis_loaded == True:
                                scr_file.write(prev_c_ld)
                        asset_prefix = line.replace('"','').replace('ld r,:a;image\\tachi\\','').replace('.jpg,','').replace('.png,','')
                        r_typeis_loaded = True
                        type_loaded = 'r'

                    asset_in_line = asset_prefix.split("%")[0].replace('\n','')
                    asset_uppercase = asset_in_line.upper()


                    if type_loaded == 'c':
                        corrected_line = "setimg " + asset_uppercase + ".png " + "48 0\n"
                        if corrected_line == 'setimg EMPTY.png 53 0\n':
                            pass
                        else:
                            scr_file.write(corrected_line)
                            prev_c_ld = corrected_line

                    elif type_loaded == 'l':
                        corrected_line = "setimg " + asset_uppercase + ".png " + "-24 0\n"
                        if corrected_line == 'setimg EMPTY.png -24 0\n':
                            pass
                        else:
                            scr_file.write(corrected_line)
                            prev_ld = corrected_line
                            prev_l_ld = corrected_line

                    elif type_loaded == 'r':
                        corrected_line = "setimg " + asset_uppercase + ".png " + "117 0\n"
                        if corrected_line == 'setimg EMPTY.png 117 0\n':
                            pass
                        else:
                            scr_file.write(corrected_line)
                            prev_ld = corrected_line
                            prev_r_ld = corrected_line
                elif line.startswith('cl r'):
                    corrected_line = actual_bg
                    r_typeis_loaded = False
                    scr_file.write(corrected_line)
                    if c_typeis_loaded and l_typeis_loaded:
                        scr_file.write(prev_c_ld)
                        scr_file.write(prev_l_ld)
                    elif c_typeis_loaded:
                        scr_file.write(prev_c_ld)
                    elif l_typeis_loaded:
                        scr_file.write(prev_l_ld)
                    else:
                        pass                
                elif line.startswith('cl l'):
                    corrected_line = actual_bg
                    l_typeis_loaded = False
                    scr_file.write(corrected_line)
                    if r_typeis_loaded and c_typeis_loaded:
                        scr_file.write(prev_r_ld)
                        scr_file.write(prev_c_ld)
                    elif r_typeis_loaded:
                        scr_file.write(prev_r_ld)
                    elif c_typeis_loaded:
                        scr_file.write(prev_c_ld)
                    else:
                        pass 
                elif line.startswith('cl c'):
                    corrected_line = actual_bg
                    c_typeis_loaded = False
                    scr_file.write(corrected_line)
                    if r_typeis_loaded and l_typeis_loaded:
                        scr_file.write(prev_r_ld)
                        scr_file.write(prev_l_ld)
                    elif r_typeis_loaded:
                        scr_file.write(prev_r_ld)
                    elif l_typeis_loaded:
                        scr_file.write(prev_l_ld)
                    else:
                        pass
                elif line.startswith("cl a"):
                    corrected_line = actual_bg
                    c_typeis_loaded = False
                    l_typeis_loaded = False
                    r_typeis_loaded = False
                    scr_file.write(corrected_line)
                elif line.startswith("wave "):
                    if line.startswith("wave se"):
                        asset_in_line = line.replace('wave ', '').replace('\n','')
                        asset_prefix = asset_in_line.replace('se','SE_')[:3].upper()
                        asset_index = asset_in_line.replace('se','')
                        asset_new_index = int(asset_index)+1
                        corrected_line = f"sound {asset_prefix}0{asset_new_index}.ogg 1\n"
                        scr_file.write(corrected_line)
                    else:
                        pass
                elif line == "br\n":
                    scr_file.write("text ~\n")
                
                elif line == "\n" or line.startswith("mov ") or line.startswith("gosub ") or line == "resettimer\n" or line.startswith("waittimer ") or line.startswith("return"):
                    pass
                elif line.startswith("!") or line.startswith("cl c") or line.startswith("cl l") or line.startswith("quakex") or line.startswith("cl r"):
                    pass
                else:
                    pass
        print("Translations finished")
        Non_exist_label = []
        Non_exist_count = 0
        for files in os.listdir(scripts):
            #(files)
            scr_file = open(scripts + files,encoding='latin-1',mode='r+').read()
            cmds_file = open(cmd_path + files,encoding='latin-1',mode='w')
            file_index = files.replace('.scr','').replace('s','').replace('\n','').replace(' ','')

            #(vars)
            ignore_read = False
            stop_write = True
            prev_cmd = ''
            choice_list = []
            dest_list = []
            prev_line = ''
            label = None
            for line in lines:
                path = None
                if line.startswith('*f'):
                    path = scripts + line.replace('*f','s').replace('\n','') + '.scr'
                if line.startswith('*f') and os.path.exists(path) == False :
                    if line not in Non_exist_label:
                        Non_exist_label.append(line)
                        Non_exist_count += 1
                        print(f'{Non_exist_count} File: {line} Not exists.')
                    else:
                        pass

                if line.startswith(';-BLOCK-') and not stop_write:
                    stop_write = True
                    break
                if line.startswith('*f'+file_index):
                    stop_write = False

                if line.startswith(';-BLOCK-') and not stop_write:
                    stop_write = True
                    break
               
                if line == 'gosub *s'+file_index+'\n':
                    cmds_file.write(scr_file)

                elif not stop_write:
                    if line == "`Você vai assistir a 'aula da Ciel-sensei'?\n":
                        corrected_line = line.replace('`','text ').replace('|','..')
                        cmds_file.write(corrected_line)
                    elif line.startswith('inc'):
                        corrected_line = line.replace('inc %', 'setvar ').replace('\n','') + ' + 1\n'
                        cmds_file.write(corrected_line)
                    elif line.startswith('goto') and not prev_cmd.startswith('jump'):

                        if line == 'goto *endofplay\n':
                            corrected_line = 'jump main.scr'
                        else:
                            corrected_line = line.replace('goto *f','jump s').replace('\n','') + '.scr'
                    
                        if corrected_line.startswith('goto'):
                            pass
                        else:
                            prev_cmd = corrected_line + '\n'
                            ignore_read = True
                            cmds_file.write(corrected_line + '\n')
                            break

                    elif line.startswith('select') and not line.startswith('selgosub'):
                        choice_list.clear()
                        dest_list.clear()
                        first_choice = line.split('`,')[0].replace('select ','').replace('`','').replace('|','..')
                        first_dest = line.split('`,')[1].replace(',','').replace('*f','s').replace('\n','') + '.scr'
                        prev_cmd = 'choice'
                        choice_list.append(first_choice)
                        dest_list.append(first_dest)

                    elif prev_cmd == 'choice' and line.startswith('\t`'):
                        choice = line.split('`,')[0][1:].replace('|','..').replace('`','')
                        choice_list.append(choice)

                        dest = line.split('`,')[1].replace('\n','').replace('*f','s').replace(',','').replace('*','') + '.scr'
                        if dest == ' endofplay.scr':
                            dest = ' main.scr'
                        dest_list.append(dest)

                        if line.endswith(',\n'):
                            pass
                        elif not line.endswith(',\n'):
                            choices = '|'.join(choice_list) + '\n'
                            corrected_line = f'choice {choices}'
                            cmds_file.write(corrected_line)

                            i = 0 
                            y = 0
                            while i < len(choice_list):
                                corrected_line = f'if selected == {i+1}\n    jump{dest_list[i]}\nfi\n'
                                cmds_file.write(corrected_line)
                                i += 1

                            choice_list.clear()
                            prev_cmd = 'Not ' + corrected_line
                    elif line.startswith('if ') and line.startswith('if %sceneskip==1') == False:
                        if_dest = None
                        if 'goto *' in line:
                            if_dest = line.split('goto *')[1].replace('f','s').replace('\n','')
                            if_condition = line.split('goto *')[0].replace('%','')
                            if '>=' in line:
                                if_condition = if_condition.replace('>=',' >= ')
                            elif '<=' in line:
                                if_condition = if_condition.replace('<=',' <= ')
                            elif '==' in line:
                                if_condition = if_condition.replace('==',' == ')
                            elif '!=' in line:
                                if_condition = if_condition.replace('!=',' != ')
                            elif '>' in line:
                                if_condition = if_condition.replace('>',' > ')
                            elif '<' in line:
                                if_condition = if_condition.replace('<',' < ')
                            
                            if '&&' in line:
                                if_condition = if_condition.replace('&&','\n    if')
                                corrected_line = f'{if_condition}\n            jump {if_dest}.scr\n    fi\nfi\n'
                            else:
                                corrected_line = f'{if_condition}\n    jump {if_dest}.scr\nfi\n'
                            cmds_file.write(corrected_line)
                    else:
                        pass
                    prev_line = line
        print('Convertion of existent files finished')
        for label in Non_exist_label:
            label_filename = label.replace('*f','s').replace('\n','') + '.scr'
            cmds_file = open(cmd_path+label_filename,encoding='latin-1',mode='w')
            file_index = label.replace('*f','').replace('s','').replace('\n','').replace(' ','')

            #(vars)
            ignore_read = False
            stop_write = True
            prev_cmd = ''
            choice_list = []
            dest_list = []
            prev_line = ''
            label = None
            for line in lines:
                path = None
                if line.startswith('*f'):
                    path = scripts + line.replace('*f','s').replace('\n','') + '.scr'
                
                if line.startswith('*f') and os.path.exists(path) == False :
                    if line not in Non_exist_label:
                        Non_exist_label.append(line)
                        Non_exist_count += 1
                        print(f'{Non_exist_count} File: {line} Not exists.')
                    else:
                        pass

                if line.startswith(';-BLOCK-') and not stop_write:
                    stop_write = True
                    break
                if line.startswith('*f'+file_index):
                    stop_write = False

                if line.startswith(';-BLOCK-') and not stop_write:
                    stop_write = True
                    break
                if line == "`Você vai assistir a 'aula da Ciel-sensei'?\n":
                    corrected_line = line.replace('`','text ').replace('|','..')
                    cmds_file.write(corrected_line)
                elif not stop_write:
                    if line.startswith('inc'):
                        corrected_line = line.replace('inc %', 'setvar ').replace('\n','') + ' + 1\n'
                        cmds_file.write(corrected_line)
                    elif line.startswith('goto') and not prev_cmd.startswith('jump'):
                        corrected_line = line.replace('goto *f','jump s').replace('\n','') + '.scr'
                    
                        if corrected_line.startswith('goto'):
                            pass
                        else:
                            prev_cmd = corrected_line + '\n'
                            ignore_read = True
                            cmds_file.write(corrected_line + '\n')
                            break
                    elif line.startswith('select') and not line.startswith('selgosub'):
                        choice_list.clear()
                        dest_list.clear()
                        first_choice = line.split('`,')[0].replace('select ','').replace('`','').replace('|','..')
                        first_dest = line.split('`,')[1].replace(',','').replace('*f','s').replace('\n','') + '.scr'
                        prev_cmd = 'choice'
                        choice_list.append(first_choice)
                        dest_list.append(first_dest)

                    elif prev_cmd == 'choice' and line.startswith('\t`'):
                        choice = line.split('`,')[0][1:].replace('|','..').replace('`','')
                        choice_list.append(choice)

                        dest = line.split('`,')[1].replace('\n','').replace('*f','s').replace(',','') + '.scr'
                        dest_list.append(dest)

                        if line.endswith(',\n'):
                            pass
                        elif not line.endswith(',\n'):
                            choices = '|'.join(choice_list) + '\n'
                            corrected_line = f'choice {choices}'
                            cmds_file.write(corrected_line)

                            i = 0 
                            y = 0
                            while i < len(choice_list):
                                corrected_line = f'if selected == {i+1}\n    jump{dest_list[i]}\nfi\n'
                                cmds_file.write(corrected_line)
                                i += 1

                            choice_list.clear()
                            prev_cmd = 'Not ' + corrected_line
                    elif line.startswith('if ') and line.startswith('if %sceneskip==1') == False:
                        if_dest = None
                        if 'goto *' in line:
                            if_dest = line.split('goto *')[1].replace('f','s').replace('\n','')
                            if_condition = line.split('goto *')[0].replace('%','')
                            if '>=' in line:
                                if_condition = if_condition.replace('>=',' >= ')
                            elif '<=' in line:
                                if_condition = if_condition.replace('<=',' <= ')
                            elif '==' in line:
                                if_condition = if_condition.replace('==',' == ')
                            elif '!=' in line:
                                if_condition = if_condition.replace('!=',' != ')
                            elif '>' in line:
                                if_condition = if_condition.replace('>',' > ')
                            elif '<' in line:
                                if_condition = if_condition.replace('<',' < ')
   
                            if '&&' in line:
                                if_condition = if_condition.replace('&&','\n    if')
                                corrected_line = f'{if_condition}\n            jump {if_dest}.scr\n    fi\nfi\n'
                            else:
                                corrected_line = f'{if_condition}\n    jump {if_dest}.scr\nfi\n'
                            cmds_file.write(corrected_line)
                    else:
                        pass
                    prev_line = line
        print("Conversion finished")
    else:
        print("Check if file " + sys.argv[1] + " exists")
else:
    print("Not enought arguments")
