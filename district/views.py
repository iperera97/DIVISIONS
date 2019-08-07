from django.shortcuts import (render, redirect, get_object_or_404, reverse)
from django.views import View
from .forms import DistrictInitForm
from django.contrib import messages
from district.models import District
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin


# view all districts
class ViewDistrct(LoginRequiredMixin, View):

    def get(self, request):

        parseData = {
            'title': 'Districts'
        }

        pageNumber = request.GET.get("page", 1)

        querySet = District.objects.all().select_related('province').order_by('pk')
        querySet = querySet.values(
            'pk',
            'sinhalaName',
            'englishName',
            'province',
            'province__englishName')

        # per page number of objects
        paginator = Paginator(querySet, 8)

        try:

            pageList = paginator.page(pageNumber)

        except PageNotAnInteger:
            pageList = paginator.page(1)

        except EmptyPage:
            pageList = paginator.page(paginator.num_pages)

        parseData['districtList'] = pageList

        return render(request, "district/home.html", parseData)


# create a new district
class CreateDistrict(LoginRequiredMixin, View):

    def get(self, request):

        parseData = {
            'title': 'Create District',
            'form': DistrictInitForm()
        }

        return render(request, "district/create.html", parseData)

    def post(self, request):

        parseData = {
            'title': 'Create District',
        }

        # requset form data and init form
        form = DistrictInitForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request, " {} District Added ".format(
                request.POST.get("englishName")))

            return redirect("district:home")

        parseData['form'] = form
        return render(request, "district/create.html", parseData)


class EditDistrict(LoginRequiredMixin, View):

    PARSE_DATA = {}

    def get(self, request, *args, **kwargs):

        # get object
        districtInstance = get_object_or_404(District, pk=kwargs.get('pk'))
        districtName = districtInstance.englishName

        # parse Data
        self.PARSE_DATA['title'] = 'Edit {} District'.format(districtName)
        self.PARSE_DATA['form'] = DistrictInitForm(instance=districtInstance)
        self.PARSE_DATA['featureImage'] = districtInstance.featureImage

        return render(request, 'district/edit.html', self.PARSE_DATA)

    # submit data
    def post(self, request, *args, **kwargs):

        # get object
        districtInstance = get_object_or_404(District, pk=kwargs.get('pk'))
        districtName = districtInstance.englishName

        # get form data and update that instance
        form = DistrictInitForm(
            request.POST,
            request.FILES,
            instance=districtInstance)

        # if success
        if form.is_valid():

            form.save()

            # success msg
            success_msg = "{} district edited".format(districtName)
            messages.success(request, success_msg)

            redirect_url = reverse('district:edit', kwargs={
                                   'pk': kwargs.get('pk')})
            return redirect(redirect_url)

        # parse Data
        self.PARSE_DATA['form'] = form
        self.PARSE_DATA['title'] = 'Edit {} District'.format(districtName)

        return render(request, 'district/edit.html', self.PARSE_DATA)


class RemoveDistrict(View):

    def get(self, request, *args, **kwargs):

        removeDistrct = get_object_or_404(District, pk=kwargs.get('pk'))
        response = removeDistrct.delete()

        # if delete count is 1 or more => success
        if response[0] >= 1:

            messages.add_message(
                request,
                messages.SUCCESS, '{} District removed'.format(
                    removeDistrct.englishName)
            )

        else:
            messages.add_message(
                request,
                messages.ERROR, '{} Distrct not removed'.format(
                    removeDistrct.englishName)
            )

        return redirect('district:home')
