"""
Management command to load initial data (Demo Day event and team members).
Run with: python manage.py load_initial_data
"""
import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import Event, TeamMember


class Command(BaseCommand):
    help = 'Load initial data for Code Vimarsh website'

    def handle(self, *args, **options):
        # Load Demo Day event
        event_description = '''Hey Everyone! 👋
It's time to showcase your hard work! We are organizing a Project Demo Day where everyone can present their projects—whether it's a finished product, a work-in-progress, or just an idea you're brainstorming. 💡

📅 Date: January 20, 2026

How to Register Your Project:
1️⃣ Open the Google Slides link above.
2️⃣ Do not edit the template directly. Instead, right-click Slide 5 and select "Duplicate Slide".
3️⃣ Fill in your project details (Name, Tech Stack, Links) on your new slide.

You'll have 4-5 minutes to present, followed by a short Q&A. 🔥

And anyone can join, whether you are building a project or just want to see what others are building!'''
        
        event, created = Event.objects.get_or_create(
            title__icontains='Demo Day',
            defaults={
                'title': 'Code Vimarsh Demo Day',
                'date': '2026-01-20',
                'description': event_description,
                'registration_link': 'https://bit.ly/vimarsh-demo-day'
            }
        )
        
        if not created:
            # Update existing event
            event.title = 'Code Vimarsh Demo Day'
            event.description = event_description
            event.registration_link = 'https://bit.ly/vimarsh-demo-day'
            event.save()
            self.stdout.write(
                self.style.SUCCESS('Successfully updated Demo Day event!')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Successfully created Demo Day event!')
            )
      
    team_members_data = [
    {'name': 'Shivam Parmar', 'role': 'President', 'gender': 'M',
     'bio': 'Leading Code Vimarsh with passion and vision. Full-stack developer with 5+ years of experience.'},

    {'name': 'Vyom Shah', 'role': 'Vice President', 'gender': 'M',
     'bio': 'Co-leading the club initiatives and organizing major events. Specializes in AI/ML and data science.'},

    {'name': 'Kirtan Soni', 'role': 'Event Head', 'gender': 'M',
     'bio': 'Handling technical workshops and hackathons. Expert in cloud computing and DevOps.'},

    {'name': 'Yash Soni', 'role': 'Management Head', 'gender': 'M',
     'bio': 'Managing community outreach and partnerships. Backend developer passionate about scalable systems.'},

    {'name': 'Maiitra Patel', 'role': 'Secretary', 'gender': 'F',
     'bio': 'Building and maintaining the club website. Frontend specialist with expertise in React and Vue.js.'},

    {'name': 'Vrunda Radadiya', 'role': 'Core Committee Member', 'gender': 'F',
     'bio': 'Full-stack developer focusing on modern web technologies.'},

    {'name': 'Khushi Patel', 'role': 'Coordinator', 'gender': 'F',
     'bio': 'Backend developer working on APIs and server infrastructure.'},

    {'name': 'Shiv Patel', 'role': 'Design Team Member', 'gender': 'M',
     'bio': 'UI/UX designer creating stunning interfaces.'},

    {'name': 'Manthan Khedekar', 'role': 'Design Team Member', 'gender': 'M',
     'bio': 'Graphic designer and brand identity specialist.'},

    {'name': 'Het Patel', 'role': 'Committee Member', 'gender': 'M',
     'bio': 'Organizing events and managing logistics.'},

    {'name': 'Kesha Babriya', 'role': 'Committee Member', 'gender': 'F',
     'bio': 'Handling social media and communications.'},

    {'name': 'Ansh Mistry', 'role': 'Committee Member', 'gender': 'M',
     'bio': 'Cybersecurity expert and ethical hacker.'},
]

    created, updated = 0, 0

    for member in team_members_data:
        obj, was_created = TeamMember.objects.update_or_create(
        name=member['name'],
        defaults={
            'role': member['role'],
            'bio': member['bio'],
            'gender': member['gender'],
        }
    )
    if was_created:
        created += 1
    else:
        updated += 1

    # self.stdout.write(
    #     self.style.SUCCESS(f'Team synced → Created: {created}, Updated: {updated}')
    # )