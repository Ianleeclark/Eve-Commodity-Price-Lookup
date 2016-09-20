
import os


def traverse_tree(root_directory, file_ext='.staticdata'):
    """
    Handles recursively traversing the tree seeking files to
    parse.

    :param str root_directory:
    :rtype: list[str]
    :return: A list of files (including their directory) which
    will be parsed.
    """
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(file_ext):
                yield '{0}/{1}'.format(root, file)


def convert_sde_to_json(file_name):
    """
    Handles converting **ALL** sde files to single json file which
    can be loaded/re-loaded at will.

    :param str file_name: The directory and file name of the SDE file to
    convert to json
    :rtype: PLEASE NOTE:
        list[
            {
                id: <int>// The EVE system ID.
                security: <float> // The security level.
                name: <string> // The name of the solar system.
                neighbors: [
                    {
                        id: <int> // The connected Eve system IDs.
                    }
                ]
            }
        ]
    :return:
    """
    with open(file_name) as f:
        out_dict = {}

        for line in f.readlines():
            if line.startswith('security: '):
                out_dict['security'] = line.split(':')[1]

if __name__ == '__main__':
    DIR = 'C:\\Users\\ilcia\\Downloads\\sde'
    with open('out.json', 'a+') as f:
        for file in traverse_tree(DIR):
            f.write(convert_sde_to_json(file))
