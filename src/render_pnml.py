"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

print "[PYTHON] render pnml"

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os.path
currentdir = os.curdir
src_path = os.path.join(currentdir, 'src')

# set output path for generated_pnml, clean it if it exists, create it if it doesn't
pnml_output_path = os.path.join(currentdir, 'generated_pnml')
if os.path.exists(pnml_output_path):
    shutil.rmtree(pnml_output_path)
os.mkdir(pnml_output_path)

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(src_path, 'templates'), format='text')
industry_templates = PageTemplateLoader(os.path.join(src_path, 'industries'), format='text')
header_item_templates = PageTemplateLoader(os.path.join(src_path, 'header_items'), format='text')

import global_constants as global_constants
import utils as utils
import firs
import cargos
from cargos import registered_cargos
import industries
from industries import registered_industries

header_items = ['checks','conditions','header','master_control_program','parameters']
for header_item in header_items:
    template = header_item_templates[header_item + '.pypnml']
    templated_pnml = utils.unescape_chameleon_output(template(registered_industries=registered_industries, global_constants=global_constants))
    # save the results of templating
    pnml = codecs.open(os.path.join(pnml_output_path, header_item + '.pnml'), 'w','utf8')
    pnml.write(templated_pnml)
    pnml.close()

template = templates['registered_cargos.pypnml']
templated_pnml = utils.unescape_chameleon_output(template(registered_cargos=registered_cargos, global_constants=global_constants))
# save the results of templating
pnml = codecs.open(os.path.join(pnml_output_path, 'registered_cargos.pnml'), 'w','utf8')
pnml.write(templated_pnml)
pnml.close()

for industry in industries.registered_industries:
    pnml = industry.render_pnml()
    # save the results of templating
    pnml_file = codecs.open(os.path.join(pnml_output_path, industry.id + '.pnml'), 'w','utf8')
    pnml_file.write(pnml)
    pnml_file.close()
