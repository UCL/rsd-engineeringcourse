import rsdpandoc.builders
import rsdpandoc.globbers

env=Environment(tools=['default',rsdpandoc.builders.add_builders])
env["HavePIL"]=False
env["HaveWSD"]=False
env["HaveWebKit"]=False

sources = [
	Glob("session0*/*.md"),
]

rsdpandoc.globbers.mixed_html_layout(sources,env,asset_sources="session*/figures")
#rsdpandoc.globbers.latex_layout(sources,env,asset_sources="session*/figures")
#rsdpandoc.globbers.latex_layout(sources,env)
