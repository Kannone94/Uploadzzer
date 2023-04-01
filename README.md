<h1>Uploadzzer</h1>
<div class="">This is a Python program that performs web requests to an uploader, fuzzing the various extensions and formats of the files to find any vulnerabilities in the upload management.</div>
<h2>Requirements</h2>
<div class="">In order to run this program, you will need the following libraries:</div>
<ol class="my-2">
<li class="ml-4 flex gap-2"><div class="rounded-full h-1 w-1 bg-white/70 mt-[10px] "></div>requests</li>
<li class="ml-4 flex gap-2"><div class="rounded-full h-1 w-1 bg-white/70 mt-[10px] "></div>argparse</li>
</ol>
<div class="">You can install them using pip:</div>
<pre>pip install -r requirements.txt</pre>
<h2>Usage</h2>
<div class="">To use this program, simply run the following command:</div>
<pre><span>python uploadzzer.py -u &lt;url&gt; -f &lt;path/to/file&gt; -e &lt;error in response&gt; --permitted &lt;formats&gt;</span></pre>
<div class="">Where:</div>
<ol class="my-2">
<li class="ml-4 flex gap-2"><div class="rounded-full h-1 w-1 bg-white/70 mt-[10px] "></div><code class="text-white bg-[#29282c] px-1 rounded">&lt;url&gt;</code> is the URL of the uploader</li>
<li class="ml-4 flex gap-2"><div class="rounded-full h-1 w-1 bg-white/70 mt-[10px] "></div><code class="text-white bg-[#29282c] px-1 rounded">&lt;path&gt;</code> is the path to the file that will be uploaded</li>
<li><code>&lt;extensions&gt;</code> is a space-separated list of extensions to be fuzzed (e.g. <code>php jsp aspx</code>)</li>
<li><code>&lt;permitted&gt;</code> is a space-separated list of formats to be fuzzed (e.g. <code>jpg png gif</code>)</li>
</ol>
<div class="">For example:</div>
<pre><span>1</span><span>python web_fuzzer.py -u http://example.com/upload.php -p /path/to/file.txt -e php,jsp,aspx -f jpg,png,gif</span></span></code></pre></div></pre>
<h2>Acknowledgements</h2>
<div class="">The methods implemented in this program were based on the following guide: <a target="_blank" class="text-blue-400 hover:text-blue-500 underline transition duration-200 ease-in-out" href="https://book.hacktricks.xyz/pentesting-web/file-upload" rel="noreferrer">https://book.hacktricks.xyz/pentesting-web/file-upload</a>.</div>
