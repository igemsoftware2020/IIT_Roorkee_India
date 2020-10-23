from rest_framework import viewsets, status
from rest_framework.response import Response
from ..serializers import JobSerializer
from ...models import Job
import os
import shutil

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def create(self, request):
        bacteria = self.request.data.get("bacteria")
        email_id = self.request.data.get("email_id")
        new_job = Job.objects.create(
            bacteria=bacteria,
            email_id=email_id
        )
        new_job.save()
        new_job_id = new_job.id
        new_job_bacteria = new_job.bacteria
        new_job_email_id = new_job.email_id

        # Directory
        directory = str(f"{new_job_id}_folder")
        current_directory = os.getcwd()
        # Parent Directory path
        parent_dir = f"{current_directory}/tailscout_app/"

        # Path
        path = os.path.join(parent_dir, directory)

        try:
            os.makedirs(path, exist_ok=True)
            print("Directory '%s' created successfully" % directory)
        except OSError as error:
            print("Directory '%s' can not be created" % directory)


        os.chdir(f"{current_directory}/tailscout_app/")



        files = ['genee.py', 'clustalo.py', 'phage_details.csv', 'jpred.pl','sequence_phages.fasta']
        for f in files:
            shutil.copy(f, f"{new_job_id}_folder")


        dname = os.path.dirname(__file__)
        fname1 = os.path.join(dname, f'../../{new_job_id}_folder/genee.py')
        fname2 = os.path.join(dname, f'../../{new_job_id}_folder/clustalo.py')
        fname3 = os.path.join(dname, f'../../{new_job_id}_folder/jpred.pl')

        os.chdir(f"{current_directory}/tailscout_app/{new_job_id}_folder")

        print(os.getcwd())

        os.system(f"python {fname1} --bacteria '{new_job_bacteria}' --filename {new_job_id}")
        # new_job_id.fasta created
        new_job.status = "S1"
        print("Step 1 done.")
        new_job.save()

        files = [f'{new_job_id}.fasta']
        for f in files:
            shutil.copy(f, f"{new_job_id}_folder")

        os.system(f"python {fname2} --email {new_job_email_id} --sequence {new_job_id}.fasta")
        # new_job_id_ABC.fasta created
        new_job.status = "S2"
        print("Step 2 done!")
        new_job.save()

        if bacteria == "acinetobacter baumannii":
            file = open(f"{new_job_id}a.fasta", "w+")
            L = [">MTTNTPKYGGLLTDIGAAALATASAAGKKWQPTHMLIGDAGGAPGDTPDPLPSAAQKSLI" + "\n" + "NQRHRAQLNRLFVSDKNANTLVAEVVLPVEVGGFWIREIGLQDADGKFVAVSNCPPSYKA" + "\n" + "AMESGSARTQTIRVNIALSGLENVQLLIDNGIIYATQDWVKEKVAADFKGRKILAGNGLL" + "\n" + "GGGDLSADRSIGLAPSGVTAGSYRSVTVNANGVVTQGSNPTTLAGYAIGDAYTKADTDGK" + "\n" +  "LAQKANKATTLAGYGITDALRVDGNAVSSSRLAAPRSLAASGDASWSVTFDGSANVSAPL" + "\n" + "SLSATGVAAGSYPKVTVDTKGRVTAGMALAATDIPGLDASKLVSGVLAEQRLPVFARGLA" + "\n" + "TAVSNSSDPNTATVPLMLTNHANGPVAGRYFYIQSMFYPDQNGNASQIATSYNATSEMYV" + "\n" + "RVSYAANPSIREWLPWQRCDIGGSFTKEADGELPGGVNLDSMVTSGWWSQSFTAQAASGA" + "\n" + "NYPIVRAGLLHVYAASSNFIYQTYQAYDGESFYFRCRHSNTWFPWRRMWHGGDFNPSDYL" + "\n" + "LKSGFYWNALPGKPATFIPTATSTTAGITKVLNVLNSNDVGSALSAAQGKVLNDKFNFQN" + "\n" +  "SKNQSGYVRLGDSGLIIQWGVFTSTKTQSNLIFPLAFPNALLSITGNLNSNTPDVIGIDF" + "\n" + "DLSTATKTSIKTGAAQVGASWLSGKKISWIAIGY"]
            file.writelines(L)
            file.close()

        files = [f'{new_job_id}a.fasta']
        for f in files:
            shutil.copy(f, f"{new_job_id}_folder")

        os.system(f"perl {fname3} submit file={new_job_id}a.fasta mode=single format=fasta email={new_job_email_id} ")
        new_job.status = "S3"
        print("Step 3 done!")

        txt_file = f"{os.getcwd()}/url.txt"
        with open(txt_file, 'r') as txtfile:
            data = txtfile.read()
            url = data.split('\\n')[0]

        new_job.save()

        return Response(
                {'url': url},
                status=status.HTTP_200_OK
        )
