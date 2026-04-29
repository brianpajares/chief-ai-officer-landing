import sys

html_file = 'code.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_nav = '''<div class="hidden md:flex space-x-8">
<a class="text-neutral-400 hover:text-neutral-100 font-serif text-sm tracking-wide hover:text-amber-400 transition-all duration-300" href="#problem">Problema</a>
<a class="text-neutral-400 hover:text-neutral-100 font-serif text-sm tracking-wide hover:text-amber-400 transition-all duration-300" href="#methodology">Metodología</a>
<a class="text-neutral-400 hover:text-neutral-100 font-serif text-sm tracking-wide hover:text-amber-400 transition-all duration-300" href="#chapters">Capítulos</a>
<a class="text-neutral-400 hover:text-neutral-100 font-serif text-sm tracking-wide hover:text-amber-400 transition-all duration-300" href="#magnet">Capítulo Gratis</a>
<a class="text-neutral-400 hover:text-neutral-100 font-serif text-sm tracking-wide hover:text-amber-400 transition-all duration-300" href="#contacto">Contacto</a>
</div>'''

old_nav = '''<div class="hidden md:flex space-x-8">
<a class="text-neutral-400 hover:text-neutral-100 font-serif text-sm tracking-wide hover:text-amber-400 transition-all duration-300" href="#problem">The Problem</a>
<a class="text-neutral-400 hover:text-neutral-100 font-serif text-sm tracking-wide hover:text-amber-400 transition-all duration-300" href="#methodology">Methodology</a>
<a class="text-neutral-400 hover:text-neutral-100 font-serif text-sm tracking-wide hover:text-amber-400 transition-all duration-300" href="#chapters">Chapters</a>
</div>'''

content = content.replace(old_nav, new_nav)

new_sections = '''
<!-- Methodology Section -->
<section class="py-section-gap px-margin-mobile md:px-margin-desktop bg-surface-container-low" id="methodology">
    <div class="max-w-container-max mx-auto">
        <div class="text-center mb-16 max-w-3xl mx-auto">
            <h2 class="font-headline-md text-headline-md text-on-surface mb-6">El método del Chief AI Officer</h2>
            <p class="font-body-md text-body-md text-on-surface-variant">Seis pasos para transformar conocimiento en resultados.</p>
        </div>
        <div class="grid md:grid-cols-2 gap-gutter">
            <div class="space-y-6">
                <!-- Method steps -->
                <div class="glass-card p-6 rounded-lg border-l-4 border-l-primary-container">
                    <h4 class="font-button text-button text-primary-container mb-2">01 Claridad</h4>
                    <p class="font-body-sm text-body-sm text-on-surface-variant">Define el problema correcto antes de tocar herramientas.</p>
                </div>
                <div class="glass-card p-6 rounded-lg border-l-4 border-l-primary-container">
                    <h4 class="font-button text-button text-primary-container mb-2">02 Criterio</h4>
                    <p class="font-body-sm text-body-sm text-on-surface-variant">Separa hechos, supuestos, inferencias y riesgos.</p>
                </div>
                <div class="glass-card p-6 rounded-lg border-l-4 border-l-primary-container">
                    <h4 class="font-button text-button text-primary-container mb-2">03 Sistema</h4>
                    <p class="font-body-sm text-body-sm text-on-surface-variant">Convierte prompts útiles en procesos repetibles.</p>
                </div>
                <div class="glass-card p-6 rounded-lg border-l-4 border-l-primary-container">
                    <h4 class="font-button text-button text-primary-container mb-2">04 Cultura</h4>
                    <p class="font-body-sm text-body-sm text-on-surface-variant">Lleva la IA del uso individual al aprendizaje colectivo.</p>
                </div>
                <div class="glass-card p-6 rounded-lg border-l-4 border-l-primary-container">
                    <h4 class="font-button text-button text-primary-container mb-2">05 Escala</h4>
                    <p class="font-body-sm text-body-sm text-on-surface-variant">Transforma conocimiento en activos y modelos de negocio.</p>
                </div>
                <div class="glass-card p-6 rounded-lg border-l-4 border-l-primary-container">
                    <h4 class="font-button text-button text-primary-container mb-2">06 Gobernanza</h4>
                    <p class="font-body-sm text-body-sm text-on-surface-variant">Avanza rápido sin perder confianza ni control.</p>
                </div>
            </div>
            <!-- Chapters list -->
            <div id="chapters" class="glass-card-premium p-8 rounded-xl h-fit">
                <h3 class="font-headline-sm text-headline-sm text-on-surface mb-6">Capítulos del Libro</h3>
                <ul class="space-y-4">
                    <li class="flex justify-between items-center border-b border-outline-variant/30 pb-2">
                        <span class="font-body-sm text-on-surface"><span class="text-primary-container font-bold mr-3">01</span>La nueva frontera del liderazgo</span>
                    </li>
                    <li class="flex justify-between items-center border-b border-outline-variant/30 pb-2">
                        <span class="font-body-sm text-on-surface"><span class="text-primary-container font-bold mr-3">02</span>El mapa estratégico de la IA</span>
                    </li>
                    <li class="flex justify-between items-center border-b border-outline-variant/30 pb-2">
                        <span class="font-body-sm text-on-surface"><span class="text-primary-container font-bold mr-3">03</span>Productividad ejecutiva</span>
                    </li>
                    <li class="flex justify-between items-center border-b border-outline-variant/30 pb-2">
                        <span class="font-body-sm text-on-surface"><span class="text-primary-container font-bold mr-3">04</span>Decisiones aumentadas</span>
                    </li>
                    <li class="flex justify-between items-center border-b border-outline-variant/30 pb-2">
                        <span class="font-body-sm text-on-surface"><span class="text-primary-container font-bold mr-3">05</span>Innovación y modelos de negocio</span>
                    </li>
                    <li class="flex justify-between items-center border-b border-outline-variant/30 pb-2">
                        <span class="font-body-sm text-on-surface"><span class="text-primary-container font-bold mr-3">06</span>Equipos y cultura</span>
                    </li>
                    <li class="flex justify-between items-center border-b border-outline-variant/30 pb-2">
                        <span class="font-body-sm text-on-surface"><span class="text-primary-container font-bold mr-3">07</span>Operaciones y escalabilidad</span>
                    </li>
                    <li class="flex justify-between items-center border-b border-outline-variant/30 pb-2">
                        <span class="font-body-sm text-on-surface"><span class="text-primary-container font-bold mr-3">08</span>Marketing y ventas</span>
                    </li>
                    <li class="flex justify-between items-center border-b border-outline-variant/30 pb-2">
                        <span class="font-body-sm text-on-surface"><span class="text-primary-container font-bold mr-3">09</span>Riesgos y gobernanza</span>
                    </li>
                    <li class="flex justify-between items-center border-b border-outline-variant/30 pb-2 border-b-0">
                        <span class="font-body-sm text-on-surface"><span class="text-primary-container font-bold mr-3">10</span>El plan de 90 días</span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- Author Section -->
<section class="py-section-gap px-margin-mobile md:px-margin-desktop bg-surface-container-lowest" id="autor">
    <div class="max-w-container-max mx-auto glass-card-premium p-12 rounded-xl border border-primary-container/20">
        <div class="grid md:grid-cols-3 gap-8 items-center">
            <div class="md:col-span-1 flex flex-col items-center">
                <!-- Placeholder for Author image -->
                <div class="w-48 h-48 rounded-full bg-surface-container-high border-2 border-primary-container mb-4 overflow-hidden flex items-center justify-center">
                    <span class="material-symbols-outlined text-6xl text-primary-container">person</span>
                </div>
                <h3 class="font-headline-sm text-on-surface font-bold">Brian Pajares</h3>
                <span class="text-primary-container font-body-sm uppercase tracking-widest mt-1">Autor</span>
            </div>
            <div class="md:col-span-2 space-y-4">
                <div class="text-primary-container uppercase font-label-caps tracking-widest">Sobre el autor</div>
                <p class="font-body-lg text-on-surface-variant">Ingeniero mecánico, ejecutivo de innovación y especialista en transformación digital y estrategia tecnológica. <b>Combina experiencia en proyectos, negocios, automatización e inteligencia artificial aplicada</b> para ayudar a profesionales y empresas a competir mejor en la nueva era digital.</p>
                <p class="font-body-lg text-on-surface-variant">Este libro es la destilación de años llevando equipos y organizaciones a través de cambios reales — donde la tecnología solo sirve cuando se traduce en resultados.</p>
            </div>
        </div>
    </div>
</section>

<!-- Magnet Section -->
<section class="py-section-gap px-margin-mobile md:px-margin-desktop bg-surface-container-highest relative overflow-hidden" id="magnet">
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom_left,_var(--tw-gradient-stops))] from-primary-container/20 via-background to-background -z-10"></div>
    <div class="max-w-container-max mx-auto">
        <div class="glass-card p-12 rounded-xl text-center max-w-3xl mx-auto border-t-2 border-primary-container shadow-2xl shadow-primary-container/10">
            <div class="text-primary-container uppercase font-label-caps tracking-widest mb-4">Recurso Exclusivo</div>
            <h2 class="font-headline-md text-headline-md text-on-surface mb-4">Descarga el primer capítulo gratis</h2>
            <p class="font-body-md text-body-md text-on-surface-variant mb-8">Déjame tus datos y te enviaré de inmediato el PDF con el capítulo 1 y la plantilla de productividad ejecutiva.</p>
            <form class="space-y-4 max-w-md mx-auto text-left">
                <div>
                    <label class="block font-label-caps text-label-caps text-on-surface-variant mb-2">Nombre completo</label>
                    <input type="text" class="w-full bg-surface border border-outline-variant rounded px-4 py-3 text-on-surface focus:border-primary focus:ring-1 focus:ring-primary" placeholder="Tu nombre" required>
                </div>
                <div>
                    <label class="block font-label-caps text-label-caps text-on-surface-variant mb-2">Email profesional</label>
                    <input type="email" class="w-full bg-surface border border-outline-variant rounded px-4 py-3 text-on-surface focus:border-primary focus:ring-1 focus:ring-primary" placeholder="tu@empresa.com" required>
                </div>
                <div class="pt-2">
                    <button type="submit" class="w-full bg-primary-container text-on-primary-container font-button text-button py-4 rounded hover:scale-[1.02] transition-transform font-bold">
                        Enviar material gratis →
                    </button>
                </div>
            </form>
        </div>
    </div>
</section>

<!-- FAQ Section -->
<section class="py-section-gap px-margin-mobile md:px-margin-desktop bg-surface-container-low" id="faq">
    <div class="max-w-container-max mx-auto max-w-4xl">
        <div class="text-center mb-16">
            <h2 class="font-headline-md text-headline-md text-on-surface mb-6">Preguntas Frecuentes</h2>
            <p class="font-body-md text-body-md text-on-surface-variant">Lo que necesitas saber antes de comprar.</p>
        </div>
        <div class="space-y-4">
            <details class="glass-card p-6 rounded-lg group cursor-pointer" open>
                <summary class="font-headline-sm text-on-surface font-semibold list-none flex justify-between items-center">
                    ¿Necesito conocimientos técnicos para aprovechar el libro?
                    <span class="material-symbols-outlined text-primary-container group-open:rotate-180 transition-transform">expand_more</span>
                </summary>
                <p class="mt-4 font-body-md text-on-surface-variant">No. La promesa del libro es clara: no necesitas convertirte en programador para liderar con IA. Sí necesitas convertirte en mejor arquitecto de preguntas, procesos, decisiones y sistemas.</p>
            </details>
            <details class="glass-card p-6 rounded-lg group cursor-pointer">
                <summary class="font-headline-sm text-on-surface font-semibold list-none flex justify-between items-center">
                    ¿Es un libro teórico o aplicable?
                    <span class="material-symbols-outlined text-primary-container group-open:rotate-180 transition-transform">expand_more</span>
                </summary>
                <p class="mt-4 font-body-md text-on-surface-variant">Aplicable. Cada capítulo trae frameworks, prompts, checklists y ejercicios. Al final tendrás un plan de 90 días, un caso de uso implementable y una matriz de riesgos.</p>
            </details>
            <details class="glass-card p-6 rounded-lg group cursor-pointer">
                <summary class="font-headline-sm text-on-surface font-semibold list-none flex justify-between items-center">
                    ¿En qué formatos está disponible?
                    <span class="material-symbols-outlined text-primary-container group-open:rotate-180 transition-transform">expand_more</span>
                </summary>
                <p class="mt-4 font-body-md text-on-surface-variant">Kindle (eBook), tapa blanda y audiolibro — todo desde la página de Amazon. Puedes alternar formatos según tu hábito de lectura.</p>
            </details>
        </div>
    </div>
</section>

<!-- Contact Section -->
<section class="py-section-gap px-margin-mobile md:px-margin-desktop bg-surface-container-highest" id="contacto">
    <div class="max-w-container-max mx-auto">
        <div class="text-center mb-16 max-w-3xl mx-auto">
            <h2 class="font-headline-md text-headline-md text-on-surface mb-6">¿Querés hablar con Brian?</h2>
            <p class="font-body-md text-body-md text-on-surface-variant">Conferencias, consultoría o simplemente una pregunta. Dejá tus datos y te respondo personalmente.</p>
        </div>
        <div class="grid md:grid-cols-2 gap-gutter">
            <div class="glass-card p-8 rounded-lg space-y-8">
                <div class="flex items-center gap-4">
                    <span class="material-symbols-outlined text-primary-container text-4xl">mail</span>
                    <div>
                        <div class="font-label-caps text-on-surface-variant tracking-widest uppercase">Email</div>
                        <div class="font-body-lg text-on-surface font-semibold">brian@brianpajares.com</div>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <span class="material-symbols-outlined text-primary-container text-4xl">public</span>
                    <div>
                        <div class="font-label-caps text-on-surface-variant tracking-widest uppercase">Disponibilidad</div>
                        <div class="font-body-lg text-on-surface font-semibold">LATAM · USA · España</div>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <span class="material-symbols-outlined text-primary-container text-4xl">calendar_today</span>
                    <div>
                        <div class="font-label-caps text-on-surface-variant tracking-widest uppercase">Temas</div>
                        <div class="font-body-lg text-on-surface font-semibold">Conferencias · Consultoría · Entrevistas</div>
                    </div>
                </div>
            </div>
            <form class="glass-card p-8 rounded-lg space-y-4">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <input type="text" class="w-full bg-surface border border-outline-variant rounded px-4 py-3 text-on-surface focus:border-primary focus:ring-1 focus:ring-primary" placeholder="Nombre completo" required>
                    </div>
                    <div>
                        <input type="email" class="w-full bg-surface border border-outline-variant rounded px-4 py-3 text-on-surface focus:border-primary focus:ring-1 focus:ring-primary" placeholder="Email profesional" required>
                    </div>
                </div>
                <div>
                    <textarea class="w-full bg-surface border border-outline-variant rounded px-4 py-3 text-on-surface h-32 focus:border-primary focus:ring-1 focus:ring-primary" placeholder="¿En qué puedo ayudarte?" required></textarea>
                </div>
                <button type="submit" class="w-full bg-primary-container text-on-primary-container font-button text-button py-4 rounded hover:scale-[1.02] transition-transform font-bold">
                    Enviar mensaje →
                </button>
            </form>
        </div>
    </div>
</section>
</main>
'''

content = content.replace('</main>', new_sections)

# Let's fix the footer links as well
old_footer_links = '''<a class="font-serif text-xs uppercase tracking-widest text-neutral-500 hover:text-amber-500 transition-colors" href="#">The Problem</a>
<a class="font-serif text-xs uppercase tracking-widest text-neutral-500 hover:text-amber-500 transition-colors" href="#">Methodology</a>
<a class="font-serif text-xs uppercase tracking-widest text-neutral-500 hover:text-amber-500 transition-colors" href="#">Chapters</a>
<a class="font-serif text-xs uppercase tracking-widest text-neutral-500 hover:text-amber-500 transition-colors" href="#">Privacy Policy</a>'''

new_footer_links = '''<a class="font-serif text-xs uppercase tracking-widest text-neutral-500 hover:text-amber-500 transition-colors" href="#problem">Problema</a>
<a class="font-serif text-xs uppercase tracking-widest text-neutral-500 hover:text-amber-500 transition-colors" href="#methodology">Metodología</a>
<a class="font-serif text-xs uppercase tracking-widest text-neutral-500 hover:text-amber-500 transition-colors" href="#chapters">Capítulos</a>
<a class="font-serif text-xs uppercase tracking-widest text-neutral-500 hover:text-amber-500 transition-colors" href="#contacto">Contacto</a>'''

content = content.replace(old_footer_links, new_footer_links)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated code.html successfully")
